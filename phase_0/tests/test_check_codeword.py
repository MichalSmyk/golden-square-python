from lib.check_codeword import *

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_with_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

def test_with_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."