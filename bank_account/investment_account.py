from bank_account.bank_account import BankAccount
from datetime import datetime

class InvestmentAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        """
        Initialize a new InvestmentAccount instance.

        Args:
            account_number (int): The account's unique number.
            client_number (int): The client's unique number.
            balance (float): The account balance.
            date_created (str): The date the account was created in "YYYY-MM-DD" format.
            management_fee (float): The management fee for the account.

        Raises:
            ValueError: If the date_created is not in the correct format.
        """
        super().__init__(account_number, client_number, balance)
        self._management_fee = management_fee
        
        # Validate date_created
        try:
            self._date_created = datetime.strptime(date_created, "%Y-%m-%d")
        except ValueError:
            raise ValueError("date_created must be in 'YYYY-MM-DD' format.")

    @property
    def management_fee(self):
        return self._management_fee

    def get_service_charges(self):
        if (datetime.now() - self._date_created).days > 3650:  # More than 10 years
            return 0.0
        return self.management_fee

    def __str__(self):
        return super().__str__() + f"Management Fee: ${self._management_fee:.2f}\n"
