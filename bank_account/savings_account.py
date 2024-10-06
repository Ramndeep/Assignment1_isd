from bank_account.bank_account import BankAccount
from datetime import datetime

class SavingsAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, interest_rate, date_created):
        super().__init__(account_number, client_number, balance)

        # Validate and set interest rate
        if not isinstance(interest_rate, (int, float)):
            raise ValueError("Interest rate must be a number.")
        self._interest_rate = float(interest_rate)

        # Validate and set creation date
        if not isinstance(date_created, str):
            raise ValueError("Date created must be a string in YYYY-MM-DD format.")
        self._date_created = datetime.strptime(date_created, "%Y-%m-%d")

    @property
    def interest_rate(self):
        return self._interest_rate

    def calculate_interest(self):
        """Calculates the interest based on the current balance."""
        return self.balance * (self.interest_rate / 100)

    def __str__(self):
        return super().__str__() + f"Interest Rate: {self._interest_rate}%\n"

