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
    def test_valid_account(self):
        account = SavingsAccount(20020, 1011, 1500.00, 2.5, "2022-01-01")
        self.assertEqual(account.account_number, 20020)
        self.assertEqual(account.client_number, 1011)
        self.assertEqual(account.balance, 1500.00)
        self.assertEqual(account.interest_rate, 2.5)

    def test_invalid_interest_rate(self):
        with self.assertRaises(ValueError):
            SavingsAccount(20020, 1011, 1500.00, "invalid_rate", "2022-01-01")

    def test_invalid_date_created(self):
        with self.assertRaises(ValueError):
            SavingsAccount(20020, 1011, 1500.00, 2.5, 12345)

    def test_calculate_interest(self):
        account = SavingsAccount(20020, 1011, 2000.00, 5.0, "2022-01-01")
        self.assertAlmostEqual(account.calculate_interest(), 100.0)  # 5% of 2000 is 100

    def test_str_method(self):
        account = SavingsAccount(20020, 1011, 1500.00, 2.5, "2022-01-01")
        expected_str = ("Account Number: 20020, Client Number: 1011, Balance: $1500.00\n"
                        "Interest Rate: 2.5%\n")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()

