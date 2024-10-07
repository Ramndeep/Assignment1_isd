"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Your Name}
Date: {Date}
"""

# 1. Import all BankAccount types using the bank_account package
from bank_account import ChequingAccount, SavingsAccount, InvestmentAccount
from datetime import datetime

# 2. Create an instance of a ChequingAccount
chequing_account = ChequingAccount(
    account_number=1234567,
    client_number=1,
    balance=-50.0,
    overdraft_limit=-100.0,
    overdraft_rate=0.05,
    date_created="2023-01-01"
)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)

# 3b. Print the service charges amount
chequing_service_charge = chequing_account.get_service_charges()
print(f"Service Charges: {chequing_service_charge}")

# 4a. Deposit enough money into the account
chequing_account.deposit(60.0)  # Adjusting balance to avoid overdraft fees

# 4b. Print the ChequingAccount
print(chequing_account)

# 4c. Print service charges after deposit
chequing_service_charge = chequing_account.get_service_charges()
print(f"Service Charges after deposit: {chequing_service_charge}")

print("===================================================")

# 5. Create an instance of a SavingsAccount
savings_account = SavingsAccount(
    account_number=9876543,
    client_number=2,
    balance=150.0,
    minimum_balance=100.0
)

# 6. Print the SavingsAccount created in step 5.
print(savings_account)

# 6b. Print the service charges amount
savings_service_charge = savings_account.get_service_charges()
print(f"Service Charges: {savings_service_charge}")

# 7a. Withdraw enough money to fall below minimum balance
savings_account.withdraw(100.0)

# 7b. Print the SavingsAccount
print(savings_account)

# 7c. Print service charges after withdrawal
savings_service_charge = savings_account.get_service_charges()
print(f"Service Charges after withdrawal: {savings_service_charge}")

print("===================================================")

# 8. Create an instance of an InvestmentAccount
investment_account_recent = InvestmentAccount(
    account_number=2345678,
    client_number=3,
    balance=500.0,
    date_created="2022-01-01",
    management_fee=10.0
)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account_recent)

# 9b. Print service charges for the recent account
investment_service_charge_recent = investment_account_recent.get_service_charges()
print(f"Service Charges: {investment_service_charge_recent}")

# 10. Create an instance of an InvestmentAccount older than 10 years
investment_account_old = InvestmentAccount(
    account_number=3456789,
    client_number=4,
    balance=300.0,
    date_created="2010-01-01",
    management_fee=15.0
)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_old)

# 11b. Print service charges for the old account
investment_service_charge_old = investment_account_old.get_service_charges()
print(f"Service Charges: {investment_service_charge_old}")

print("===================================================")

# 12. Withdraw service charges if applicable
# For ChequingAccount
if chequing_service_charge > 0:
    chequing_account.withdraw(chequing_service_charge)
    print("After adjusting for service charges (Chequing):")
    print(chequing_account)

# For SavingsAccount
if savings_service_charge > 0:
    savings_account.withdraw(savings_service_charge)
    print("After adjusting for service charges (Savings):")
    print(savings_account)

# For InvestmentAccount (recent)
if investment_service_charge_recent > 0:
    investment_account_recent.withdraw(investment_service_charge_recent)
    print("After adjusting for service charges (recent Investment):")
    print(investment_account_recent)

# For InvestmentAccount (old)
if investment_service_charge_old > 0:
    investment_account_old.withdraw(investment_service_charge_old)
    print("After adjusting for service charges (old Investment):")
    print(investment_account_old)

print("===================================================")


