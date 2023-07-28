from lib.count_words import count_words

"""
A function called count_words that takes a string as an argument and
returns the number of words in that string.
"""

#takes empty string and returns 0
def test_given_empty_string_returns_0():
    result = count_words(" ")
    assert result == 0

#returns a number of words in a string
def test_given_a_string_returns_numbers_of_words_in_it():
    result = count_words("one two three")
    assert result == 3