from lib.todo import Todo

"""
Initialises with task set to false
"""

def test_initialises_with_a_task_set_to_false():
    todo = Todo("clean room")
    assert todo.complete == False

"""
sets the complete to True
"""

def test_sets_the_complete_to_true():
    todo = Todo("walk the cat")
    todo.mark_complete()
    assert todo.complete == True