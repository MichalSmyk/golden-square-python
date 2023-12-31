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
    
#get error if wrapping alredy wrapped 
def test_wrapping_alredy_wrapped():
    present = Present()
    present.wrap(1)
    with pytest.raises(Exception) as e:
        present.wrap(2)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

#if we try to wrap an already wrapped present first wrappec valu is unchanged
def test_wrapping_alredy_wrapped_preserves_value():
    present = Present()
    present.wrap(1)
    with pytest.raises(Exception) as e:
        present.wrap(2)
    assert present.unwrap() == 1