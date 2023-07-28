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

"""
Given a valid sentence with a capital letter and a question mark
Returns true
"""
def test_with_capital_letter_and_question_mark():
    result = grammar_check("Hello, this is correct sentence?")
    assert result == True

"""
Given a valid sentence with a capital letter and a exclamation mark
Returns true
"""
def test_with_capital_letter_and_exclamation_mark():
    result = grammar_check("Hello, this is correct sentence!")
    assert result == True

"""
Given a sentence with capittal letter but ends with a coma 
Returns false 
"""
def test_with_capital_letter_but_ending_with_comma():
    result = grammar_check("Hello, this is incorrect sentence,")
    assert result == False

"""
Given with no capital letter and a full stop
Returns false
"""
def test_with_lower_letter_and_stop():
    result = grammar_check("hello, this is incorrect sentence.")
    assert result == False
