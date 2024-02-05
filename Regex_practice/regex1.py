# extracting email
import re

def extract_emails(email):
  pattern = re.compile(r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$')

  match = pattern.findall(email)
  return match
text = "Contact us at john.doe@example.com or support@company.org for assistance."
result = extract_emails(text)
print(result)