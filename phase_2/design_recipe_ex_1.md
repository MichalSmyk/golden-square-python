# Reading time Function Design Recipe


## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python


def reading_time(text):
    """Given a text user wants to know how long it will take to read.
        200 word per minute

    Parameters: (list all parameters and their types)
        text: a string containing words 

    Returns: (state the return value and its type)
        returns time in minutes

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
Given no text
It returns 0
"""
reading_time("") => 0

"""
Given 100 words
It returns 0.5
"""
reading_time("assume 100 words here") => 0.5

"""
Given 200 words 
It returns 1
"""
reading_time("assume 200 words here") => 1

"""
Given 300 words 
It returns 1.5
"""
reading_time("assume 300 words here") => 1.5

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.reading_time import *

"""
Given a text 
It returns how long it takes to read it when 200 words takes one minute
"""
def test_given_zero_words():
    result = reading_time("")
    assert result == 0

```

Ensure all test function names are unique, otherwise pytest will ignore them!


