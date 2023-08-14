from lib.task_tracker import TaskTracker

"""
Initially, there are no tasks
"""
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

"""
When we add a task
It is reflected in the lost of tasks
"""
def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

# """
# When we add multiple tasks
# They are all reflected in the list of tasks 
# """
# tracekr = TaskTracker()
# tracker.add("Walk a dog")
# tracker.add("Walk a cat")
# tracker.add("Walk a frog")
# tracker.list_incomplete() #=> ["Walk the dog", "Walk a cat", "Walk a frog"]

# """
# When we add multiple tasks
# And mark one as complete 
# It disappears from the task list
# """
# tracekr = TaskTracker()
# tracker.add("Walk a dog")
# tracker.add("Walk a cat")
# tracker.add("Walk a frog")
# tracker.makr_complete(1)
# tracker.list_incomplete() #=> ["Walk the dog", "Walk a frog"]

# """
# If we try to mark a task tomplete that does not exist 
# it rises an error 
# """
# tracekr = TaskTracker()
# tracker.add("Walk a dog")
# tracker.mark_complete(-1) # Raises an error "No such task to mark complete"
# tracker.list_incomplete() #=> ["Walk the dog"]

# """
# If we try to mark a task tomplete that does not exist 
# it rises an error 
# """
# tracekr = TaskTracker()
# tracker.add("Walk a dog")
# tracker.mark_complete(2) # Raises an error "No such task to mark complete"
# tracker.list_incomplete() #=> ["Walk the dog"]