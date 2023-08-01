# Todo Function Design Recipe



## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def todo_checker(text):
    """checks that the text contains word todo
    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a boolean

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text with uppercase word
It returns true
"""
todo_checker("This string contains #TODO") => True

"""
Given a text with lowercase word
It returns true
"""
todo_checker("This string contains #todo") => True

"""
Given a text without hash tag but uppercase
It returns false
"""
todo_checker("This string contains wrong TODO") => False

"""
Given a text without hash tag but in lower case 
It returns false
"""
todo_checker("This string contains wrong todo") => False

"""
Given a text without a string in upper case 
It returns false
"""
todo_checker("This string does not contain a key word") => False

"""
Given a text without a string in lower case 
It returns false
"""
todo_checker("This string does not contain a key word") => False

"""
Given an empty string
It returns false
"""
todo_checker("") => False

"""
Given a None value
It throws an error
"""
todo_checker(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.todo_checker import *

"""
Given a text with uppercase word
It returns true
"""
def test_contains_necesary_string():
    result = todo_checker("This string contains #TODO")
    assert result == True

```

Ensure all test function names are unique, otherwise pytest will ignore them!
