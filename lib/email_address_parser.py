import re

# class EmailAddressParser:
#     def __init__(self, email_string):
#         self.email_string = email_string

#     def parse(self):
#         email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#         email_addresses = re.findall(email_pattern, self.email_string)
#         return email_addresses
class EmailAddressParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
            # Use regular expression to find email addresses in the input string
        email_pattern = r'\S+@\S+'
        emails = re.findall(email_pattern, self.input_string)

            # Use regular expression to find email addresses in the input string
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, self.input_string)

        # Remove any trailing commas or spaces from the found email addresses
        cleaned_emails = [email.strip(' ,') for email in emails]

            # Remove empty strings (non-email strings)
        valid_emails = [email for email in cleaned_emails if email]

            # Sort the list of valid email addresses
        valid_emails.sort()

        return valid_emails