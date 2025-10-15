import { Configuration, PlaidApi, PlaidEnvironments, Products, CountryCode } from 'plaid';
import { config } from '../config/config';

class PlaidService {
  private client: PlaidApi;
  private mockMode: boolean;

  constructor() {
    this.mockMode = config.plaid.mockMode;

    if (!this.mockMode) {
      const configuration = new Configuration({
        basePath: PlaidEnvironments[config.plaid.env],
        baseOptions: {
          headers: {
            'PLAID-CLIENT-ID': config.plaid.clientId,
            'PLAID-SECRET': config.plaid.secret,
          },
        },
      });
      this.client = new PlaidApi(configuration);
    }
  }

  async createLinkToken(userId: string): Promise<string> {
    if (this.mockMode) {
      return this.createMockLinkToken(userId);
    }

    try {
      const response = await this.client.linkTokenCreate({
        user: { client_user_id: userId },
        client_name: 'Banking App',
        products: [Products.Transactions, Products.Auth],
        country_codes: [CountryCode.Us],
        language: 'en',
      });

      return response.data.link_token;
    } catch (error) {
      console.error('Plaid link token error:', error);
      throw error;
    }
  }

  async exchangePublicToken(publicToken: string) {
    if (this.mockMode) {
      return this.exchangeMockPublicToken(publicToken);
    }

    try {
      const response = await this.client.itemPublicTokenExchange({
        public_token: publicToken,
      });

      return {
        accessToken: response.data.access_token,
        itemId: response.data.item_id,
      };
    } catch (error) {
      console.error('Plaid token exchange error:', error);
      throw error;
    }
  }

  async getAccounts(accessToken: string) {
    if (this.mockMode) {
      return this.getMockAccounts();
    }

    try {
      const response = await this.client.accountsGet({ access_token: accessToken });
      return response.data.accounts;
    } catch (error) {
      console.error('Plaid get accounts error:', error);
      throw error;
    }
  }

  async getTransactions(accessToken: string, startDate: string, endDate: string) {
    if (this.mockMode) {
      return this.getMockTransactions(startDate, endDate);
    }

    try {
      const response = await this.client.transactionsGet({
        access_token: accessToken,
        start_date: startDate,
        end_date: endDate,
      });

      return response.data.transactions;
    } catch (error) {
      console.error('Plaid get transactions error:', error);
      throw error;
    }
  }

  // Mock implementations
  private createMockLinkToken(userId: string): string {
    return `link-sandbox-${userId}-${Date.now()}`;
  }

  private exchangeMockPublicToken(publicToken: string) {
    return {
      accessToken: `access-sandbox-${Date.now()}`,
      itemId: `item-sandbox-${Date.now()}`,
    };
  }

  private getMockAccounts() {
    return [
      {
        account_id: 'mock-checking-001',
        name: 'Checking Account',
        official_name: 'Premium Checking',
        type: 'depository',
        subtype: 'checking',
        mask: '0000',
        balances: {
          current: 2540.76,
          available: 2540.76,
          iso_currency_code: 'USD',
        },
      },
      {
        account_id: 'mock-savings-001',
        name: 'Savings Account',
        official_name: 'High Yield Savings',
        type: 'depository',
        subtype: 'savings',
        mask: '1111',
        balances: {
          current: 15200.50,
          available: 15200.50,
          iso_currency_code: 'USD',
        },
      },
      {
        account_id: 'mock-credit-001',
        name: 'Credit Card',
        official_name: 'Rewards Credit Card',
        type: 'credit',
        subtype: 'credit card',
        mask: '2222',
        balances: {
          current: -845.32,
          available: 4154.68,
          limit: 5000,
          iso_currency_code: 'USD',
        },
      },
    ];
  }

  private getMockTransactions(startDate: string, endDate: string) {
    const transactions = [];
    const categories = [
      { name: 'Groceries', category: ['Food and Drink', 'Groceries'] },
      { name: 'Gas Station', category: ['Transportation', 'Gas'] },
      { name: 'Restaurant', category: ['Food and Drink', 'Restaurants'] },
      { name: 'Amazon', category: ['Shops', 'Online'] },
      { name: 'Netflix', category: ['Entertainment', 'Streaming'] },
      { name: 'Gym Membership', category: ['Recreation', 'Gyms'] },
      { name: 'Salary Deposit', category: ['Income', 'Payroll'] },
    ];

    // Generate mock transactions
    for (let i = 0; i < 50; i++) {
      const category = categories[Math.floor(Math.random() * categories.length)];
      const isIncome = category.name === 'Salary Deposit';
      const amount = isIncome
        ? -3500 - Math.random() * 500  // Negative for income in Plaid
        : 10 + Math.random() * 200;

      transactions.push({
        transaction_id: `mock-txn-${i}`,
        account_id: 'mock-checking-001',
        amount,
        date: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
        name: category.name,
        merchant_name: category.name,
        category: category.category,
        pending: Math.random() > 0.9,
        payment_channel: 'online',
      });
    }

    return transactions.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }
}

export default new PlaidService();

