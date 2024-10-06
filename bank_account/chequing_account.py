from bank_account.bank_account import BankAccount
from datetime import datetime

class ChequingAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, overdraft_limit, overdraft_rate, date_created):
        super().__init__(account_number, client_number, balance)
        
        # Validate and set overdraft limit
        if not isinstance(overdraft_limit, (int, float)):
            raise ValueError("Overdraft limit must be a number.")
        self._overdraft_limit = float(overdraft_limit)

        # Validate and set overdraft rate
        if not isinstance(overdraft_rate, (int, float)):
            raise ValueError("Overdraft rate must be a number.")
        self._overdraft_rate = float(overdraft_rate)

        # Validate and set creation date
        if not isinstance(date_created, str):
            raise ValueError("Date created must be a string in YYYY-MM-DD format.")
        self._date_created = datetime.strptime(date_created, "%Y-%m-%d")

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @property
    def overdraft_rate(self):
        return self._overdraft_rate

    def get_service_charges(self):
        # Service charge logic based on balance relative to overdraft limit
        if self.balance > self.overdraft_limit:
            return 0.0
        elif self.balance < self.overdraft_limit:
            return self.overdraft_rate
        return 0.0

    def __str__(self):
        return super().__str__() + f"Overdraft Limit: ${self._overdraft_limit}, Overdraft Rate: ${self._overdraft_rate}\n"
