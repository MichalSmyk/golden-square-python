from lib.todo import Todo
from lib.todo_list import TodoList

"""
Adds one todo to the list
I can see it in the incomplete list
"""
def test_adds_one_todo_and_lists_it():
    todo_list = TodoList()    
    todo_1 = Todo("walk the dog")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]
"""
Adds two todos 
I can see them back in the incomplete list
"""

def test_adds_and_lists_todos():
    todo_list = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("walk the cat")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]
