from lib.string_builder import *

#starts with empty string
def test_string_builder_init_with_empty_string():
    builder = StringBuilder()
    assert builder.output() == ""
#length for empty string
def test_length_of_empty_string_is_zero():
    builder = StringBuilder()
    assert builder.size() == 0