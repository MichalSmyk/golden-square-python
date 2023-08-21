from lib.todo_list import TodoList

"""
Initialises with empty todo list
"""

def test_initialises_with_empty_list():
    todo_list = TodoList()
    assert todo_list._todo == []

