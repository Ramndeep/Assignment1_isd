# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Ramandeep kaur

## Assignment
Assignment 1: Classes, Encapsulation, and Unit Test Planning

## Encapsulation

### Client Class
Encapsulation in the `Client` class is achieved by:
- **Private Attributes**: `client_number`, `first_name`, `last_name`, and `email_address` are private attributes. Access to these attributes is controlled through getter methods.
- **Validation**: The constructor validates inputs to ensure that `client_number` is numeric, names are not blank, and email addresses follow a valid format. If invalid, appropriate exceptions are raised or default values are assigned.
- **Default Values**: Invalid email addresses are set to a default value to ensure consistency.

### BankAccount Class
Encapsulation in the `BankAccount` class is achieved by:
- **Private Attributes**: `account_number`, `client_number`, and `balance` are private attributes. Access is controlled via getter methods.
- **Methods for Updating Balance**: The `deposit` and `withdraw` methods handle balance updates while ensuring that only valid transactions are processed. Non-numeric inputs are rejected, and exceptions are raised for invalid operations such as overdrafts or negative amounts.
- **Validation**: The constructor validates that `account_number` and `client_number` are numeric and that the initial balance is a valid number. If invalid, a `ValueError` is raised.

### Running the Tests
To execute all tests, use the following command:
```sh
python -m unittest discover -s tests