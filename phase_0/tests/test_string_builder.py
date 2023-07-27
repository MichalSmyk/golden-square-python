from lib.string_builder import *

def test_string_builder_init_with_empty_string():
    builder = StringBuilder()
    assert builder.output() == ""