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
        account.deposit
