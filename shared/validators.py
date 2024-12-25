import re
from django.core.exceptions import ValidationError

class StrongPasswordValidator:
    def __init__(self, min_length=10):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(f"Password must be at least {self.min_length} characters long.")

        # At least one lowercase letter
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")

        # At least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        # At least one digit
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain at least one number.")

        # At least one special character
        if not re.search(r'[\W_]', password):  # \W matches any non-alphanumeric character
            raise ValidationError("Password must contain at least one special character.")

    def get_help_text(self):
        return (
            f"Your password must be at least {self.min_length} characters long, "
            "contain at least one lowercase letter, one uppercase letter, one digit, and one special character."
        )
