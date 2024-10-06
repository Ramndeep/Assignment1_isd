import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import datetime, timedelta

class TestInvestmentAccount(unittest.TestCase):
    def test_valid_account(self):
        """Test that a valid InvestmentAccount can be created."""
        date_created = "2020-01-01"
        account = InvestmentAccount(20019, 1010, 1500.00, date_created, 0.03)
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(account.balance, 1500.00)
        self.assertEqual(account.management_fee, 0.03)

    def test_service_charge_old_account(self):
        """Test service charge for accounts older than 10 years."""
        date_created = (datetime.now() - timedelta(days=3651)).strftime("%Y-%m-%d")
        account = InvestmentAccount(20019, 1010, 800.00, date_created, 0.03)
        self.assertEqual(account.get_service_charges(), 0.0)

    def test_service_charge_new_account(self):
        """Test service charge for accounts younger than 10 years."""
        date_created = "2022-01-01"
        account = InvestmentAccount(20019, 1010, 800.00, date_created, 0.03)
        self.assertEqual(account.get_service_charges(), 0.03)

    def test_invalid_date_created(self):
        """Test that an invalid date raises a ValueError."""
        with self.assertRaises(ValueError):
            InvestmentAccount(20019, 1010, 1500.00, "not_a_date", 0.03)

    def test_negative_management_fee(self):
        """Test that a negative management fee raises a ValueError."""
        with self.assertRaises(ValueError):
            InvestmentAccount(20019, 1010, 1500.00, "2020-01-01", -0.01)

    def test_str_method(self):
        """Test the string representation of the account."""
        date_created = "2020-01-01"
        account = InvestmentAccount(20019, 1010, 1500.00, date_created, 0.03)
        expected_str = (
            "Account Number: 20019, Client Number: 1010, Balance: $1,500.00\n"
            "Management Fee: $0.03\n"
        )
        self.assertEqual(str(account), expected_str)

    def test_management_fee_getter(self):
        """Test that the management fee getter works correctly."""
        date_created = "2020-01-01"
        account = InvestmentAccount(20019, 1010, 1500.00, date_created, 0.03)
        self.assertEqual(account.management_fee, 0.03)

    def test_edge_case_service_charge(self):
        """Test the service charge for accounts exactly 10 years old."""
        date_created = (datetime.now() - timedelta(days=3650)).strftime("%Y-%m-%d")
        account = InvestmentAccount(20019, 1010, 800.00, date_created, 0.03)
        self.assertEqual(account.get_service_charges(), 0.03)

if __name__ == '__main__':
    unittest.main()
