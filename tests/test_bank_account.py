"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Ramandeep kaur
Date: 15 September 2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_valid_account(self):
        account = BankAccount(20019, 1010, 6764.67)
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(account.balance, 6764.67)

    def test_deposit(self):
        account = BankAccount(20019, 1010, 6764.67)
        account.deposit(500.00)
        self.assertEqual(account.balance, 7264.67)
        with self.assertRaises(ValueError):
            account.deposit(-100.00)

    def test_withdraw(self):
        account = BankAccount(20019, 1010, 6764.67)
        account.withdraw(1000.00)
        self.assertEqual(account.balance, 5764.67)
        with self.assertRaises(ValueError):
            account.withdraw(-100.00)
        with self.assertRaises(ValueError):
            account.withdraw(7000.00)

    def test_str_method(self):
        account = BankAccount(20019, 1010, 6764.67)
        self.assertEqual(str(account), "Account Number: 20019, Client Number: 1010, Balance: $6764.67")

    def test_non_numeric_balance(self):
        with self.assertRaises(ValueError):
            BankAccount(20019, 1010, "not_a_number")

    def test_invalid_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount("not_a_number", 1010, 6764.67)

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(20019, "not_a_number", 6764.67)

if __name__ == "__main__":
    unittest.main()