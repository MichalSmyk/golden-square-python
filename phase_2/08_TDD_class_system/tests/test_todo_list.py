from lib.todo_list import TodoList
from lib.todo import Todo
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
    todo = Todo("walk the dog")
    todo_list.add(todo)
    assert todo_list.incomplete() == [todo]

"""
Adds two tasks to the inpomplete list
"""
def test_adds_tasks_to_incomplete_list():
    todo_list = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("walk the cat")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]

