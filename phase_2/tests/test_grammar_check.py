from lib.grammar_check import *

"""
Given a valid sentence with a capital letter and a full stop
Returns true
"""
def test_with_valid_sentence():
    result = grammar_check("Hello, this is correct sentence.")
    assert result == True