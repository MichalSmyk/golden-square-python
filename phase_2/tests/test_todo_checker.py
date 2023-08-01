from lib.todo_checker import *

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