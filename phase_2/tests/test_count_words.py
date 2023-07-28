from lib.count_words import count_words

"""
A function called count_words that takes a string as an argument and
returns the number of words in that string.
"""

#takes empty string and returns it 
def test_given_empty_string_returns_it():
    result = count_words("")
    assert result == ""

