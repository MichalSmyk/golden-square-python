from lib.todo_checker import *
import pytest
"""
Given a text 
It returns false
"""
def test_contains_string():
    result = todo_checker("This string is a text")
    assert result == False

    """
Given a text with uppercase word
It returns true
"""
def test_text_contains_uppercase_todo():
    result = todo_checker("This string contains #TODO")
    assert result == True

"""
Given a text with lowercase word
It returns true
"""
def test_text_contains_lowercase_todo():
    result = todo_checker("This string contains #todo")
    assert result == True

"""
Given a text without hash tag but uppercase
It returns false
"""
def test_todo_in_upper_but_missing_hashtag():
    result = todo_checker("This string contains wrong TODO")
    assert result == False

"""
Given a text without hash tag but in lower case 
It returns false
"""
def test_todo_in_lower_missing_tag():
    result = todo_checker("This string contains wrong todo") 
    assert result == False

"""
Given an empty string
It returns false
"""
def test_with_empty_string():
    result = todo_checker("")
    assert result == False

"""
Given a None value
It throws an error
"""
def test_given_a_non_value_throws_error():
    # result = todo_checker(None)
    with pytest.raises(Exception) as e:
        todo_checker(None)
    error_message = str(e.value)
    assert error_message == "Please provide a string"
