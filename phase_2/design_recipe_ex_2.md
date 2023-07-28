# Grammar check Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_check(text):
    """
    Parameters: 
        text: a string representing a human-readable text
    Returns:
        boolean, true if valid, false otherwise
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a valid sentence with a capital letter and a full stop
Returns true
"""
grammar_check("Hello, this is correct sentence.")
# => True
"""
Given a valid sentence with a capital letter and a question mark
Returns true
"""
grammar_check("Hello, this is correct sentence?")
# => True
"""
Given a valid sentence with a capital letter and a exclamation mark
Returns true
"""
grammar_check("Hello, this is correct sentence!")
# => True
"""
Given a sentence with capital letter but not fill stop or other mark
Returns false 
"""
grammar_check("Hello, this is correct sentence")
# => False

"""
Given with no capital letter and a full stop
Returns false
"""
grammar_check("hello, this is correct sentence")
# => False

"""
Given a sentence with capittal letter but ends with a coma 
Returns false 
"""
grammar_check("Hello, this is correct sentence,")
# => False

"""
Given no sentence 
Raises an error 
"""
grammar_check("")
# Raises "Cannot check grammar of empty string"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

