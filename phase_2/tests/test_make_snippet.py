from lib.make_snippet import *

#takes an empty string and returns it 
def test_given_empty_string_returns_it():
    result = make_snippet("")
    assert result == ""