# extracting email
# # r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$'
import re

def extract_emails(email):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    match = pattern.findall(email)
    return match
text = "Contact us at john.doe@example.com or support@company.org for assistance."
result = extract_emails(text)
print(result)