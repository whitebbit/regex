import pytest
from regex_utils import find_emails, validate_date_format, extract_email_parts, validate_phone_number, split_sentences

import re


def test_find_emails():
    text = "Sample text with emails: user@example.com, john.doe@mail.org"
    assert find_emails(text) == ['user@example.com', 'john.doe@mail.org']


def test_validate_date_format():
    assert validate_date_format("12/25/2023") == True
    assert validate_date_format("02/28/2024") == True
    assert validate_date_format("13/01/2022") == False


def test_extract_email_parts():
    email = "user@example.com"
    assert extract_email_parts(email) == {'username': 'user', 'domain': 'example.com'}


def test_validate_phone_number():
    assert validate_phone_number("+1-1234567890") == True
    assert validate_phone_number("123-456-7890") == False
    assert validate_phone_number("+123-456-789012345") == False


def test_split_sentences():
    text = "This is sentence one. And this is sentence two? Finally, sentence three."
    assert split_sentences(text) == ["This is sentence one.", "And this is sentence two?", "Finally, sentence three."]


if __name__ == '__main__':
    pytest.main()
