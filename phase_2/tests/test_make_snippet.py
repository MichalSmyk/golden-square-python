from lib.make_snippet import *

#takes an empty string and returns it 
def test_given_empty_string_returns_it():
    result = make_snippet("")
    assert result == ""

#given a string of one word returns it 
def test_given_one_word_returns_it():
    result = make_snippet("Hello")
    assert result == "Hello"

"""
if given more than 5 words first returns 
first 5 words and ...
"""
def test_if_more_than_5_words_returns_5_and_dots():
    result = make_snippet("Hello how are you feeling today")
    assert result == "Hello how are you feeling..."