from lib.todo import Todo
from lib.todo_list import TodoList

"""
Adds two todos 
I can see them back in the incomplete list
"""

def test_adds_and_lists_todos():
    todo_list = TodoList()
    todo = Todo("walk the dog")
    todo_list.add(todo)
    assert todo_list.incomplete() == [todo]
