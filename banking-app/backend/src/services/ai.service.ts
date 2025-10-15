import OpenAI from 'openai';
import { config } from '../config/config';

class AIService {
  private openai: OpenAI;
  private model: string;

  constructor() {
    this.openai = new OpenAI({ 
      apiKey: config.openai.apiKey,
      baseURL: config.openai.baseURL,
      defaultHeaders: {
        'HTTP-Referer': 'http://localhost:3001',
        'X-Title': 'Banking App AI',
      }
    });
    this.model = config.openai.model;
  }

  async categorizeTransaction(transactionName: string, amount: number, existingCategory?: string[]): Promise<{ category: string; subcategory: string }> {
    try {
      const prompt = `Categorize this transaction:
Transaction: ${transactionName}
Amount: $${amount}
${existingCategory ? `Plaid Category: ${existingCategory.join(' > ')}` : ''}

Provide a more specific category and subcategory for personal finance tracking.
Respond in JSON format: {"category": "...", "subcategory": "..."}

Categories should be one of: Food & Dining, Shopping, Transportation, Bills & Utilities, Entertainment, Healthcare, Travel, Income, Savings, Other`;

      const response = await this.openai.chat.completions.create({
        model: this.model,
        messages: [
          { role: 'system', content: 'You are a financial categorization expert.' },
          { role: 'user', content: prompt },
        ],
        temperature: 0.3,
        max_tokens: 100,
      });

      const content = response.choices[0].message.content || '{}';
      const parsed = JSON.parse(content);
      
      return {
        category: parsed.category || 'Other',
        subcategory: parsed.subcategory || 'Miscellaneous',
      };
    } catch (error) {
      console.error('AI categorization error:', error);
      return { category: 'Other', subcategory: 'Miscellaneous' };
    }
  }

  async generateFinancialInsights(transactions: any[], budgets: any[]): Promise<string[]> {
    try {
      const prompt = `Analyze these financial transactions and budgets, provide 3-5 actionable insights:

Transactions summary:
- Total transactions: ${transactions.length}
- Total spent: $${transactions.filter(t => t.amount > 0).reduce((sum, t) => sum + t.amount, 0).toFixed(2)}
- Top categories: ${this.getTopCategories(transactions, 3)}

Budgets: ${budgets.map(b => `${b.category}: $${b.amount}/${b.period}`).join(', ')}

Provide insights as a JSON array of strings.`;

      const response = await this.openai.chat.completions.create({
        model: this.model,
        messages: [
          { role: 'system', content: 'You are a personal financial advisor.' },
          { role: 'user', content: prompt },
        ],
        temperature: 0.7,
        max_tokens: 500,
      });

      const content = response.choices[0].message.content || '[]';
      return JSON.parse(content);
    } catch (error) {
      console.error('AI insights error:', error);
      return ['Unable to generate insights at this time.'];
    }
  }

  async predictFutureExpenses(transactions: any[]): Promise<{ category: string; predicted: number }[]> {
    // Simple prediction based on historical averages
    const categorySpending: Record<string, number[]> = {};

    transactions.forEach(t => {
      if (t.amount > 0 && t.aiCategory) {
        if (!categorySpending[t.aiCategory]) {
          categorySpending[t.aiCategory] = [];
        }
        categorySpending[t.aiCategory].push(t.amount);
      }
    });

    return Object.entries(categorySpending).map(([category, amounts]) => ({
      category,
      predicted: amounts.reduce((sum, amt) => sum + amt, 0) / amounts.length,
    }));
  }

  async detectUnusualActivity(transaction: any, historicalTransactions: any[]): Promise<{ isUnusual: boolean; reason?: string }> {
    // Simple heuristic: check if amount is significantly higher than average
    const similarTransactions = historicalTransactions.filter(
      t => t.aiCategory === transaction.aiCategory
    );

    if (similarTransactions.length < 5) {
      return { isUnusual: false };
    }

    const avgAmount = similarTransactions.reduce((sum, t) => sum + t.amount, 0) / similarTransactions.length;
    const stdDev = Math.sqrt(
      similarTransactions.reduce((sum, t) => sum + Math.pow(t.amount - avgAmount, 2), 0) / similarTransactions.length
    );

    if (transaction.amount > avgAmount + 2 * stdDev) {
      return {
        isUnusual: true,
        reason: `This transaction is significantly higher than your average ${transaction.aiCategory} spending.`,
      };
    }

    return { isUnusual: false };
  }

  async generateSavingSuggestions(income: number, expenses: number, goals: any[]): Promise<string[]> {
    try {
      const prompt = `Based on this financial data, provide 3-5 personalized saving suggestions:

Monthly Income: $${income}
Monthly Expenses: $${expenses}
Savings Rate: ${((income - expenses) / income * 100).toFixed(1)}%
Saving Goals: ${goals.map(g => `${g.name} ($${g.targetAmount})`).join(', ')}

Provide suggestions as a JSON array of strings.`;

      const response = await this.openai.chat.completions.create({
        model: this.model,
        messages: [
          { role: 'system', content: 'You are a financial planning expert.' },
          { role: 'user', content: prompt },
        ],
        temperature: 0.7,
        max_tokens: 400,
      });

      const content = response.choices[0].message.content || '[]';
      return JSON.parse(content);
    } catch (error) {
      console.error('AI suggestions error:', error);
      return ['Consider setting up automatic transfers to your savings account.'];
    }
  }

  private getTopCategories(transactions: any[], count: number): string {
    const categoryCounts: Record<string, number> = {};
    
    transactions.forEach(t => {
      if (t.aiCategory) {
        categoryCounts[t.aiCategory] = (categoryCounts[t.aiCategory] || 0) + 1;
      }
    });

    return Object.entries(categoryCounts)
      .sort(([, a], [, b]) => b - a)
      .slice(0, count)
      .map(([cat]) => cat)
      .join(', ');
  }
}

export default new AIService();

