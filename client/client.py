"""
Description: This module contains the Client class, which represents a client in the banking system.
Author: Ramandeep kaur
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number, first_name, last_name, email_address):
        """
        Initialize a new Client instance.

        Args:
            client_number (int): The client's unique number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: If client_number is not an integer or first_name/last_name is blank.
            EmailNotValidError: If the email address is invalid.
        """
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        if not first_name.strip():
            raise ValueError("First name cannot be blank.")
        if not last_name.strip():
            raise ValueError("Last name cannot be blank.")
        try:
            valid_email = validate_email(email_address)
            self._email_address = valid_email.email
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"

        self._client_number = client_number
        self._first_name = first_name.strip()
        self._last_name = last_name.strip()

    @property
    def client_number(self):
        return self._client_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email_address(self):
        return self._email_address

    def __str__(self):
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}\n"
