def validate_password(password: str) -> str:
    if len(password) < 8:
        return "YOUR PASSWORD MUST BE 8 CHARACTERS OR MORE!"
    
    if not any(char.isupper() for char in password):
        return "YOUR PASSWORD MUST CONTAIN AT LEAST ONE UPPERCASE LETTER!"
    
    if not any(char.islower() for char in password):
        return "YOUR PASSWORD MUST CONTAIN AT LEAST ONE LOWERCASE LETTER!"
    
    if not any(char.isdigit() for char in password):
        return "YOUR PASSWORD MUST CONTAIN AT LEAST ONE DIGIT!"
    
    special_characters = "!@#$%^&*()"
    if not any(char in special_characters for char in password):
        return "YOUR PASSWORD MUST CONTAIN AT LEAST ONE OF THE SPECIAL CHARACTERS!"
    
    return "YOU HAVE A VALID PASSWORD!"
