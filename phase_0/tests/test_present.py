import pytest
from lib.present import *

#when we wrap an tiem we get it back when unwrapping
def test_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

"""
unwrap before wrapping
get error message 
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

# if wrapped twice get error message 
def test_wrap_twice():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap(1)
        present.wrap(1)
    message = str(e.value)
    assert message == "A contents has already been wrapped."
    