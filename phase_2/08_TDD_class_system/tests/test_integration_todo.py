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

"""
Marks a todo as complete 
"""

def test_marks_todo_as_complete():
    todo_list = TodoList()
    todo_1 = Todo("walk the dog")
    todo_list.add(todo_1)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]


"""
Adds two todos,
marks only one as complete 
"""

def test_adds_two_todos_but_marks_one_as_complete():
    todo_list = TodoList()
    todo_1 = Todo("walk the dog")
    todo_2 = Todo("walk the cat")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]
