
import re

def reg2(email):
    pattern = re.compile(r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$')

    if pattern.match(email):
        return True
    else:
        return False

mails=['john.doe@example.com','alice_smith123@gmail.com','bob-jones@company.org','123john@example.com','user@domain','jane@company..com']

for mail in mails:
    print(reg2(mail))