from playwright.async_api import async_playwright, Browser, Page
from typing import Dict, Optional
import logging
from app.config import settings

logger = logging.getLogger(__name__)


class AutomationService:
    """Service for browser automation using Playwright"""
    
    def __init__(self, headless: bool = None, mock_mode: bool = None):
        self.headless = headless if headless is not None else settings.HEADLESS_BROWSER
        self.mock_mode = mock_mode if mock_mode is not None else settings.MOCK_AUTOMATION
        self.browser: Optional[Browser] = None
        self.playwright = None
    
    async def initialize(self):
        """Initialize Playwright browser"""
        if self.mock_mode:
            logger.info("Running in mock automation mode")
            return
        
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=self.headless)
            logger.info("Browser initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize browser: {e}")
            self.mock_mode = True
    
    async def close(self):
        """Close browser and playwright"""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
    
    async def apply_to_job(
        self,
        job_url: str,
        user_data: Dict,
        resume_path: Optional[str] = None,
        cover_letter: Optional[str] = None
    ) -> Dict:
        """
        Apply to a job posting
        
        Args:
            job_url: URL of the job posting
            user_data: User profile data for form filling
            resume_path: Path to resume file
            cover_letter: Cover letter text
            
        Returns:
            Dict with success status and details
        """
        if self.mock_mode:
            return self._mock_apply_to_job(job_url, user_data)
        
        try:
            page = await self.browser.new_page()
            await page.goto(job_url, wait_until='networkidle')
            
            # Detect job board and apply accordingly
            if 'linkedin.com' in job_url:
                result = await self._apply_linkedin(page, user_data, resume_path)
            elif 'indeed.com' in job_url:
                result = await self._apply_indeed(page, user_data, resume_path)
            elif 'greenhouse.io' in job_url:
                result = await self._apply_greenhouse(page, user_data, resume_path, cover_letter)
            else:
                result = await self._apply_generic(page, user_data, resume_path, cover_letter)
            
            await page.close()
            return result
        
        except Exception as e:
            logger.error(f"Automation error for {job_url}: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to apply to job'
            }
    
    async def _apply_linkedin(self, page: Page, user_data: Dict, resume_path: Optional[str]) -> Dict:
        """Apply to LinkedIn job"""
        try:
            # Click Easy Apply button
            easy_apply_button = page.locator('button:has-text("Easy Apply")')
            if await easy_apply_button.count() > 0:
                await easy_apply_button.click()
                await page.wait_for_timeout(1000)
                
                # Fill in form fields
                await self._fill_common_fields(page, user_data)
                
                # Upload resume if available
                if resume_path:
                    file_input = page.locator('input[type="file"]')
                    if await file_input.count() > 0:
                        await file_input.set_input_files(resume_path)
                
                # Click through multi-page forms
                while True:
                    next_button = page.locator('button:has-text("Next"), button:has-text("Review")')
                    if await next_button.count() == 0:
                        break
                    await next_button.click()
                    await page.wait_for_timeout(1000)
                
                # Submit application
                submit_button = page.locator('button:has-text("Submit application")')
                if await submit_button.count() > 0:
                    await submit_button.click()
                    await page.wait_for_timeout(2000)
                    return {'success': True, 'message': 'Applied via LinkedIn Easy Apply'}
            
            return {'success': False, 'message': 'Easy Apply not available'}
        
        except Exception as e:
            logger.error(f"LinkedIn application error: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _apply_indeed(self, page: Page, user_data: Dict, resume_path: Optional[str]) -> Dict:
        """Apply to Indeed job"""
        try:
            # Click Apply Now button
            apply_button = page.locator('button:has-text("Apply now"), a:has-text("Apply now")')
            if await apply_button.count() > 0:
                await apply_button.click()
                await page.wait_for_timeout(1000)
                
                # Fill form fields
                await self._fill_common_fields(page, user_data)
                
                # Upload resume
                if resume_path:
                    file_input = page.locator('input[type="file"]')
                    if await file_input.count() > 0:
                        await file_input.set_input_files(resume_path)
                
                # Submit
                submit_button = page.locator('button[type="submit"], button:has-text("Submit")')
                if await submit_button.count() > 0:
                    await submit_button.click()
                    await page.wait_for_timeout(2000)
                    return {'success': True, 'message': 'Applied via Indeed'}
            
            return {'success': False, 'message': 'Apply button not found'}
        
        except Exception as e:
            logger.error(f"Indeed application error: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _apply_greenhouse(self, page: Page, user_data: Dict, resume_path: Optional[str], cover_letter: Optional[str]) -> Dict:
        """Apply to Greenhouse ATS job"""
        try:
            await self._fill_common_fields(page, user_data)
            
            # Upload resume
            if resume_path:
                resume_input = page.locator('input[name*="resume"], input[id*="resume"]')
                if await resume_input.count() > 0:
                    await resume_input.set_input_files(resume_path)
            
            # Fill cover letter
            if cover_letter:
                cover_letter_field = page.locator('textarea[name*="cover"], textarea[id*="cover"]')
                if await cover_letter_field.count() > 0:
                    await cover_letter_field.fill(cover_letter)
            
            # Submit
            submit_button = page.locator('input[type="submit"], button[type="submit"]')
            if await submit_button.count() > 0:
                await submit_button.click()
                await page.wait_for_timeout(2000)
                return {'success': True, 'message': 'Applied via Greenhouse'}
            
            return {'success': False, 'message': 'Submit button not found'}
        
        except Exception as e:
            logger.error(f"Greenhouse application error: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _apply_generic(self, page: Page, user_data: Dict, resume_path: Optional[str], cover_letter: Optional[str]) -> Dict:
        """Apply to generic job posting"""
        try:
            # Try to find and fill common form fields
            await self._fill_common_fields(page, user_data)
            
            # Upload resume if file input exists
            if resume_path:
                file_inputs = page.locator('input[type="file"]')
                count = await file_inputs.count()
                if count > 0:
                    await file_inputs.first.set_input_files(resume_path)
            
            # Fill cover letter if textarea exists
            if cover_letter:
                textareas = page.locator('textarea')
                count = await textareas.count()
                if count > 0:
                    await textareas.first.fill(cover_letter)
            
            # Try to find and click submit button
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                'button:has-text("Submit")',
                'button:has-text("Apply")',
                'a:has-text("Submit")'
            ]
            
            for selector in submit_selectors:
                button = page.locator(selector)
                if await button.count() > 0:
                    await button.first.click()
                    await page.wait_for_timeout(2000)
                    return {'success': True, 'message': 'Applied to job'}
            
            return {'success': False, 'message': 'Could not find submit button'}
        
        except Exception as e:
            logger.error(f"Generic application error: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _fill_common_fields(self, page: Page, user_data: Dict):
        """Fill common application form fields"""
        field_mappings = {
            'name': ['name', 'full name', 'fullname'],
            'email': ['email', 'e-mail'],
            'phone': ['phone', 'telephone', 'mobile'],
            'location': ['location', 'city', 'address'],
            'linkedin': ['linkedin', 'linkedin url'],
            'github': ['github', 'github url'],
            'portfolio': ['portfolio', 'website', 'personal website'],
        }
        
        for data_key, field_names in field_mappings.items():
            value = user_data.get(data_key)
            if not value:
                continue
            
            for field_name in field_names:
                # Try various selector strategies
                selectors = [
                    f'input[name*="{field_name}" i]',
                    f'input[id*="{field_name}" i]',
                    f'input[placeholder*="{field_name}" i]',
                ]
                
                for selector in selectors:
                    field = page.locator(selector)
                    if await field.count() > 0:
                        await field.first.fill(str(value))
                        break
    
    def _mock_apply_to_job(self, job_url: str, user_data: Dict) -> Dict:
        """Mock application for testing"""
        import random
        success = random.random() > 0.1  # 90% success rate for testing
        
        if success:
            return {
                'success': True,
                'message': f'Mock application submitted successfully to {job_url}',
                'applied_date': datetime.utcnow().isoformat()
            }
        else:
            return {
                'success': False,
                'error': 'Mock error: Application form validation failed',
                'message': 'Failed to apply'
            }

