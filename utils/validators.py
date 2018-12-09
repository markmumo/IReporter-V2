import re

from attr import validate


class Validate:

    def is_string(name):
        """
        username must contain only alphanumeric characters and a min of 4 character
        """
        return re.match("^[A-Za-z]{4,}$", name)

    def validate_phone_number(phoneNumber):
        """
        phone number validation, phone number must start with a digit and end with
        a digit, and must be 10 digits only in this format xxxx-xxx-xxx.
        """
        return re.match(r'^\d{4}-\d{3}-\d{3}$', phoneNumber)

    def validate_username(username):
        return re.match("^[a-zA-Z0-9]{4,}$", username)

    def validate_password(password):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)

    def validate_email(email):
        """ email must start not start with @ and can contain only one @ and must not end with @ """
        return re.match("[^@]+@[^@]+\.[^@]+$", email)

    def validate_input_strings(input_strings):
        """ input strings must start with letters and can contain alphanumeric and special characters """
        return re.match("^[a-zA-Z0-9.-_@]", input_strings)
