from lib.todo import Todo

"""
Initialises with task set to false
"""

def test_initialises_with_a_task_set_to_false():
    todo = Todo("clean room")
    assert todo == False

