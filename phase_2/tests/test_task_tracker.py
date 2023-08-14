from lib.task_tracker import TaskTracker
import pytest
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

"""
When we add multiple tasks
They are all reflected in the list of tasks 
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk a dog")
    tracker.add("Walk a cat")
    tracker.add("Walk a frog")
    assert tracker.list_incomplete() == ["Walk a dog", "Walk a cat", "Walk a frog"]

"""
When we add multiple tasks
And mark one as complete 
It disappears from the task list
"""
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("Walk a dog")
    tracker.add("Walk a cat")
    tracker.add("Walk a frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk a dog", "Walk a frog"]

"""
If we try to mark a task tomplete that does not exist 
it rises an error 
"""
def test_mark_task_tat_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add("Walk a dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1) # Raises an error "No such task to mark complete"
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk a dog"]

"""
If we try to mark a task tomplete that does not exist 
it rises an error 
"""
def test_mark_task_tat_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk a dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1) # Raises an error "No such task to mark complete"
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk a dog"]