# Task Tracker Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker():
    def add(self, task):
        #Parameters:
        #   task: string, representing a class
        pass

    def list_incomplete(self):
        #Returns:
        #   A list of incomplete tasks

    def mark_complete(self, index):
        #Parameters:
        #   index: an integer representing thetask to complete
        #Side-effect:
        #   Removes the task at index from the list of tasks
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, there are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete() #=> []

"""
When we add a task
It is reflected in the lost of tasks
"""

tracekr = TaskTracker()
tracker.add("Walk a dog")
tracker.list_incomplete() #=> ["Walk the dog"]

"""
When we add multiple tasks
They are all reflected in the list of tasks 
"""
tracekr = TaskTracker()
tracker.add("Walk a dog")
tracker.add("Walk a cat")
tracker.add("Walk a frog")
tracker.list_incomplete() #=> ["Walk the dog", "Walk a cat", "Walk a frog"]

"""
When we add multiple tasks
And mark one as complete 
It disappears from the task list
"""
tracekr = TaskTracker()
tracker.add("Walk a dog")
tracker.add("Walk a cat")
tracker.add("Walk a frog")
tracker.makr_complete(1)
tracker.list_incomplete() #=> ["Walk the dog", "Walk a frog"]

"""
If we try to mark a task tomplete that does not exist 
it rises an error 
"""
tracekr = TaskTracker()
tracker.add("Walk a dog")
tracker.mark_complete(-1) # Raises an error "No such task to mark complete"
tracker.list_incomplete() #=> ["Walk the dog"]

"""
If we try to mark a task tomplete that does not exist 
it rises an error 
"""
tracekr = TaskTracker()
tracker.add("Walk a dog")
tracker.mark_complete(2) # Raises an error "No such task to mark complete"
tracker.list_incomplete() #=> ["Walk the dog"]
 ```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

