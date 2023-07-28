from lib.grammar_check import *

"""
Given a valid sentence with a capital letter and a full stop
Returns true
"""
def test_with_valid_sentence():
    result = grammar_check("Hello, this is correct sentence.")
    assert result == True

"""
Given a sentence with capital letter but not fill stop or other mark
Returns false 
"""
def test_with_capital_letter_but_no_end_mark():
    result = grammar_check("Hello, this is incorrect sentence")
    assert result == False