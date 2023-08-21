from lib.todo_list import TodoList

"""
Initialises with empty todo list
"""

def test_initialises_with_empty_list():
    todo_list = TodoList()
    assert todo_list._todo == []

"""
Adds a task to incomplete list 
"""
def test_adds_a_task_to_incomplete_list():
    todo_list = TodoList()
    todo_list.add("walk the dog")
    assert todo_list.incomplete() == ["walk the dog"]