import secrets
import string


def generate_alphanumerical_token(length):
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    characters = string.ascii_letters + string.digits 
    return ''.join(secrets.choice(characters) for _ in range(length))