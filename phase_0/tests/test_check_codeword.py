from lib.check_codeword import *

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."