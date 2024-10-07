from bank_account.bank_account import BankAccount
from datetime import datetime

class SavingsAccount(BankAccount):
    def __init__(self, account_number, client_number, balance, minimum_balance=100.0):
        super().__init__(account_number, client_number, balance)

        self._minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self._minimum_balance

    def get_service_charges(self):
        if self.balance < self.minimum_balance:
            return 5.0  # Example service charge for falling below minimum balance
        return 0.0

    def __str__(self):
        return super().__str__() + f"Minimum Balance: ${self._minimum_balance:.2f}\n"

