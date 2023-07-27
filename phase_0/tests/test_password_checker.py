import pytest
from lib.password_checker import PasswordChecker

def test_returns_true_if_password_is_more_or_8_char():
    password = PasswordChecker()
    assert password.check("12345678") == True

def test_returns_err_msg_if_password_less_than_8_char():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("12345")
    error_msg = str(e.value)
    assert error_msg == "Invalid password, must be 8+ characters."