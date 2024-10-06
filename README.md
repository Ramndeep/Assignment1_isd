# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Ramandeep kaur

## Assignment
Assignment 2: Advanced Classes, Inheritance, Polymorphism, and Unit Testing


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

### InvestmentAccount Class
- Inherits from `BankAccount`.
- **Attributes**:
  - `management_fee`: Fee charged for managing the account.
  - `date_created`: Date when the account was opened.
- **Methods**:
  - `get_service_charges()`: Calculates service charges based on the account's age.
  - `__str__()`: Extends the string representation to include the management fee.

### ChequingAccount Class
- Inherits from `BankAccount`.
- **Description**: Represents a chequing account with specific features (to be detailed).

### SavingsAccount Class
- Inherits from `BankAccount`.
- **Description**: Represents a savings account with saving features (to be detailed).

### Running the Tests
To execute all tests, use the following command:
```sh
python -m unittest discover -s tests

## Polymorphism

Polymorphism in this project is primarily achieved through method overriding in the subclasses of the `BankAccount` class. Each subclass—`InvestmentAccount`, `ChequingAccount`, and `SavingsAccount`—inherits from `BankAccount` and can implement its own version of methods that are defined in the parent class.

### Implementation Details:

1. **Overriding Methods**:
   - Each subclass can provide its own implementation of methods such as `__str__()` to return a customized string representation of the account. For example, while the `BankAccount` class might provide a basic string format, `InvestmentAccount` can extend it to include details specific to investment accounts, such as management fees.

2. **Dynamic Method Resolution**:
   - When an account object is instantiated as either `InvestmentAccount`, `ChequingAccount`, or `SavingsAccount`, the appropriate method implementation is invoked at runtime based on the actual object type. This allows for flexibility and the ability to add new account types in the future without modifying existing code.

3. **Example**:
   - If you call the `__str__()` method on an `InvestmentAccount` object, it will execute the overridden version in `InvestmentAccount`, providing detailed information about the management fee and account creation date, whereas calling the same method on a `SavingsAccount` will provide its unique representation.

This polymorphic behavior ensures that the system is extensible and adheres to the principles of object-oriented programming, allowing for cleaner and more maintainable code.
