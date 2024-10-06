"""
Description: Unit tests for the ChequingAccount class.
Author: Your Name
Date: YYYY-MM-DD
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import datetime

class TestChequingAccount(unittest.TestCase):
    def test_valid_account(self):
        account = ChequingAccount(20019, 1010, 1500.00, 500.00, 15.00, "2022-01-01")
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(account.balance, 1500.00)
        self.assertEqual(account.overdraft_limit, 500.00)
        self.assertEqual(account.overdraft_rate, 15.00)

    def test_invalid_overdraft_limit(self):
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1500.00, "invalid", 15.00, "2022-01-01")

    def test_invalid_overdraft_rate(self):
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1500.00, 500.00, "invalid", "2022-01-01")

    def test_invalid_date_created(self):
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1500.00, 500.00, 15.00, 12345)

    def test_service_charges(self):
        account = ChequingAccount(20019, 1010, 1500.00, 500.00, 15.00, "2022-01-01")
        self.assertEqual(account.get_service_charges(), 0.0)  # Balance > Overdraft Limit

        account.withdraw(1000.00)
        self.assertEqual(account.get_service_charges(), 15.00)  # Balance < Overdraft Limit

        account.withdraw(1000.00)  # Further withdrawal to go below overdraft limit
        self.assertEqual(account.get_service_charges(), 15.00)  # Balance still < Overdraft Limit

    def test_str_method(self):
        account = ChequingAccount(20019, 1010, 1500.00, 500.00, 15.00, "2022-01-01")
        expected_str = ("Account Number: 20019, Client Number: 1010, Balance: $1500.00\n"
                        "Overdraft Limit: $500.0, Overdraft Rate: $15.0\n")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()
