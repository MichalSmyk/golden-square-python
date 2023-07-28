from lib.reading_time import *

"""
Given a text 
It returns how long it takes to read it when 200 words takes one minute
"""
def test_given_zero_words():
    result = reading_time("")
    assert result == 0
