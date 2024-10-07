"""
Description: Unit tests for the SavingsAccount class.
Author: Your Name
Date: YYYY-MM-DD
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""

import unittest
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):

    def test_init_attributes(self):
        account = SavingsAccount(12345, 67890, 500.0)
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 67890)
        self.assertEqual(account.balance, 500.0)
        self.assertEqual(account.minimum_balance, 100.0)  # Default minimum balance

    def test_init_invalid_minimum_balance(self):
        with self.assertRaises(ValueError):
            SavingsAccount(12345, 67890, 500.0, minimum_balance=-50)

    def test_get_service_charges_above_minimum(self):
        account = SavingsAccount(12345, 67890, 150.0)
        self.assertEqual(account.get_service_charges(), 0.0)

    def test_get_service_charges_equal_to_minimum(self):
        account = SavingsAccount(12345, 67890, 100.0)
        self.assertEqual(account.get_service_charges(), 0.0)

    def test_get_service_charges_below_minimum(self):
        account = SavingsAccount(12345, 67890, 50.0)
        self.assertEqual(account.get_service_charges(), 5.0)

    def test_str_method(self):
        account = SavingsAccount(12345, 67890, 500.0)
        expected_str = "Account Number: 12345 Balance: $500.00\nMinimum Balance: $100.00\n"
        self.assertEqual(str(account), expected_str)

if __name__ == "__main__":
    unittest.main()
