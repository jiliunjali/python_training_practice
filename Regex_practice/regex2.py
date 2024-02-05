# practice of regex
#validate a password
# criteria:

"""At least 8 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Contains at least one digit.
Contains at least one special character (one of !@#$%^&*)."""


import re

def reg(password):
    pattern=re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$')

    if pattern.match(password):
        return True
    else:
        return False

# Test the function with different passwords
passwords_to_test = ["Abcd123!", "StrongPassword", "weak", "Short!1"]
for password in passwords_to_test:
    result = reg(password)
    print(f"Password: {password}, Valid: {result}")