import pytest
from lib.present import *

#when we wrap an tiem we get it back when unwrapping
def test_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33