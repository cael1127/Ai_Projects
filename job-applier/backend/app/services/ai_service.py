from typing import Dict, List
from openai import OpenAI
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class AIService:
    """Service for AI-powered resume and cover letter generation"""
    
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL,
            default_headers={
                'HTTP-Referer': 'http://localhost:8001',
                'X-Title': 'AI Job Applier',
            }
        )
        self.model = settings.OPENAI_MODEL
    
    def generate_resume(
        self,
        user_profile: Dict,
        job_description: str,
        job_title: str,
        company: str
    ) -> str:
        """Generate a tailored resume for a specific job"""
        
        prompt = self._build_resume_prompt(user_profile, job_description, job_title, company)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert resume writer who creates ATS-optimized, tailored resumes."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            resume_content = response.choices[0].message.content
            return resume_content
        
        except Exception as e:
            logger.error(f"Resume generation error: {e}")
            return self._generate_fallback_resume(user_profile)
    
    def generate_cover_letter(
        self,
        user_profile: Dict,
        job_description: str,
        job_title: str,
        company: str
    ) -> str:
        """Generate a tailored cover letter for a specific job"""
        
        prompt = self._build_cover_letter_prompt(user_profile, job_description, job_title, company)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert cover letter writer who creates compelling, personalized cover letters."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            cover_letter = response.choices[0].message.content
            return cover_letter
        
        except Exception as e:
            logger.error(f"Cover letter generation error: {e}")
            return self._generate_fallback_cover_letter(user_profile, job_title, company)
    
    def analyze_job_fit(self, user_profile: Dict, job_description: str) -> Dict:
        """Analyze how well a user's profile matches a job"""
        
        prompt = f"""Analyze the fit between this candidate and job:

Candidate Profile:
- Experience: {user_profile.get('years_experience', 'N/A')} years
- Skills: {', '.join(user_profile.get('skills', []))}
- Education: {user_profile.get('education', 'N/A')}

Job Description:
{job_description}

Provide:
1. Match score (0-100)
2. Key matching strengths (3-5 points)
3. Potential gaps (2-3 points)
4. Recommendation (should apply? yes/no/maybe)

Return as JSON."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a career counselor analyzing job fit."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            
            import json
            analysis = json.loads(response.choices[0].message.content)
            return analysis
        
        except Exception as e:
            logger.error(f"Job fit analysis error: {e}")
            return {
                'match_score': 50,
                'strengths': ['Unable to analyze at this time'],
                'gaps': [],
                'recommendation': 'maybe'
            }
    
    def _build_resume_prompt(
        self,
        user_profile: Dict,
        job_description: str,
        job_title: str,
        company: str
    ) -> str:
        """Build prompt for resume generation"""
        
        return f"""Generate a professional, ATS-optimized resume tailored for this job:

Job: {job_title} at {company}
Job Description: {job_description}

Candidate Information:
- Name: {user_profile.get('full_name', 'John Doe')}
- Email: {user_profile.get('email', '')}
- Phone: {user_profile.get('phone', '')}
- Location: {user_profile.get('location', '')}
- LinkedIn: {user_profile.get('linkedin_url', '')}
- GitHub: {user_profile.get('github_url', '')}
- Years of Experience: {user_profile.get('years_experience', 0)}

Education:
{self._format_education(user_profile.get('education', []))}

Work Experience:
{self._format_work_experience(user_profile.get('work_experience', []))}

Skills:
{', '.join(user_profile.get('skills', []))}

Certifications:
{', '.join(user_profile.get('certifications', []))}

Instructions:
1. Highlight relevant skills and experiences for this specific role
2. Use keywords from the job description
3. Make it ATS-friendly
4. Keep it professional and concise
5. Emphasize achievements with metrics where possible
6. Format in clean, readable text

Generate the resume content in plain text format."""
        
    def _build_cover_letter_prompt(
        self,
        user_profile: Dict,
        job_description: str,
        job_title: str,
        company: str
    ) -> str:
        """Build prompt for cover letter generation"""
        
        return f"""Write a compelling cover letter for this job application:

Job: {job_title} at {company}
Job Description: {job_description[:500]}...

Candidate:
- Name: {user_profile.get('full_name', 'Applicant')}
- Years of Experience: {user_profile.get('years_experience', 0)}
- Top Skills: {', '.join(user_profile.get('skills', [])[:5])}

Instructions:
1. Address the hiring manager professionally
2. Express genuine interest in the role and company
3. Highlight 2-3 key qualifications that match the job
4. Include specific examples or achievements
5. Close with enthusiasm and call to action
6. Keep it to 3-4 paragraphs
7. Professional tone but personable

Generate the cover letter:"""
    
    def _format_education(self, education: List[Dict]) -> str:
        """Format education entries"""
        if not education:
            return "No education provided"
        
        formatted = []
        for edu in education:
            formatted.append(f"- {edu.get('degree', '')} in {edu.get('field', '')}, {edu.get('school', '')} ({edu.get('year', '')})")
        return '\n'.join(formatted)
    
    def _format_work_experience(self, experience: List[Dict]) -> str:
        """Format work experience entries"""
        if not experience:
            return "No work experience provided"
        
        formatted = []
        for exp in experience:
            formatted.append(f"- {exp.get('title', '')} at {exp.get('company', '')} ({exp.get('duration', '')})")
            if exp.get('achievements'):
                for achievement in exp['achievements']:
                    formatted.append(f"  * {achievement}")
        return '\n'.join(formatted)
    
    def _generate_fallback_resume(self, user_profile: Dict) -> str:
        """Generate a basic resume if AI fails"""
        name = user_profile.get('full_name', 'Job Seeker')
        email = user_profile.get('email', '')
        phone = user_profile.get('phone', '')
        
        return f"""{name}
{email} | {phone}

SUMMARY
Experienced professional seeking new opportunities.

SKILLS
{', '.join(user_profile.get('skills', ['Various skills']))}

EXPERIENCE
{self._format_work_experience(user_profile.get('work_experience', []))}

EDUCATION
{self._format_education(user_profile.get('education', []))}
"""
    
    def _generate_fallback_cover_letter(self, user_profile: Dict, job_title: str, company: str) -> str:
        """Generate a basic cover letter if AI fails"""
        name = user_profile.get('full_name', 'Applicant')
        
        return f"""Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company}. With my experience and skills, I believe I would be a valuable addition to your team.

I am excited about the opportunity to contribute to {company}'s success and would welcome the chance to discuss how my background aligns with your needs.

Thank you for considering my application. I look forward to hearing from you.

Sincerely,
{name}
"""


ai_service = AIService()

