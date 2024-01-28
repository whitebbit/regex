import re


def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


def validate_date_format(date):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/\d{4}$'
    return bool(re.match(pattern, date))


def extract_email_parts(email):
    pattern = r'(?P<username>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})'
    match = re.match(pattern, email)
    if match:
        return match.groupdict()
    return None


def validate_phone_number(phone_number):
    pattern = r'^(\+\d{1,3}-?)?\d{1,14}$'
    return bool(re.match(pattern, phone_number))


def split_sentences(text):
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    return re.split(pattern, text)
