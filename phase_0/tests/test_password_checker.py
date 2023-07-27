import pytest
from lib.password_checker import PasswordChecker

def test_returns_true_if_password_is_more_or_8_char():
    password = PasswordChecker()
    assert password.check("12345678") == True