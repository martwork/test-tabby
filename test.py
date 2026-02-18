import re

def parse_email_addresses(email_string):
    """
    This function takes a string containing one or more email addresses.
    It returns a list of the domain parts of the email addresses.
    """
    # Regular expression to match email addresses with "@" symbol
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, email_string)

    return matches

# Test the function
email_string = "Here are my emails: johndoe@example.com, jane_doe@company.com, and abc@example.net."
print(parse_email_addresses(email_string))