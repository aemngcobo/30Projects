import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        
    return False

def contains_upper(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generate_password(length: int,symbols: bool,uppercase: bool)-> str:
    combination: str= string.ascii_lowercase + string.digits
    
    if symbols:
        combination +=string.punctuation
        
        if uppercase:
    