"""
Description: This module contains the BankAccount class, which represents a bank account in the banking system.
Author: Ramandeep kaur
"""

class BankAccount:
    def __init__(self, account_number, client_number, balance):
        """
        Initialize a new BankAccount instance.

        Args:
            account_number (int): The account's unique number.
            client_number (int): The client's unique number.
            balance (float): The account balance.

        Raises:
            ValueError: If account_number or client_number is not an integer.
            ValueError: If balance cannot be converted to float.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

        self._account_number = account_number
        self._client_number = client_number

    @property
    def account_number(self):
        return self._account_number

    @property
    def client_number(self):
        return self._client_number

    @property
    def balance(self):
        return self._balance

    def update_balance(self, amount):
        """
        Update the account balance with the given amount.

        Args:
            amount (float): The amount to update the balance by.
        """
        try:
            self._balance += float(amount)
        except ValueError:
            pass

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not numeric or positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount):
        """
        Withdraw a positive amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not numeric, positive, or exceeds the balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed the account balance: ${self._balance:.2f}")
        self.update_balance(-amount)

    def __str__(self):
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
