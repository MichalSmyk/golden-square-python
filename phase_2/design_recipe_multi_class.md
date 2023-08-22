# Task Tracker Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks and see a list of them 

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them dissapear from the list

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
# Nouns
task
list of tasks
program

# Verbs 
add
see a list
marking something complete
disappear


   ┌──────────────────────────┐
   │ TaskList                 │
   │                          │
   │ - add(task)              │
   │ - list_incomplete()      │
   │ - list_complete()        │
   │                          │
   │                          │
   └────────────┬─────────────┘
                │
                │
                │
                │
    ┌───────────▼─────────────┐
    │ Task                    │
    │ - title [property]      │
    │ - initialize(title)     │
    │ - mark_complete()       │
    │ - is_complete [property]│
    │                         │
    │                         │
    └─────────────────────────┘


```

_Also design the interface of each class in more detail._

```python
class TaskList():
    def add(self, task):
        # Parameters:
        #   task: an instance of the Task class
        # Side-effects:
        #   Adds the task to an internal list of tasks
        pass

    def list_incomplete(self):
        # Returns:
        #   A list of instances of Task that are incomplete
        pass

    def list_complete(self):
        # Returns:
        #   A list of instances of Task that are complete
        pass


class Task():
    #public properties:
    #   title: a string representing a job to do
    #   complete: a boolean, true is task is complete, false otherwise
    def __init__(self, title):
        # Parameters:
        #   title: a string representing a job to do
        # Side-effects: sets the title property
        #   sets the task incomplete at first
        pass

    def mark_complete(self):
        # Side-effects: marks the task as complete
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE
"""
When I add multiple  tasks
They come back in the incomplete list
"""
tracker = TaskTracker()
task_1 = Task("Walk the dog")
taks_2 = Task("Walk the cat")
tracker.add(task_1)
tracker.add(task_2)
tracker.list_incomplete() # => [task_1, task_2]

"""
When I add multiple tasks
And makr one as complete
It does not show up in the incomplete list anymore
"""
tracker = TaskTracker()
task_1 = Task("Walk the dog")
taks_2 = Task("Walk the cat")
tracker.add(task_1)
tracker.add(task_2)
task_1.mark_complete()
tracker.list_incomplete() # => [task_2]

"""
When I add multiple tasks
And makr one as complete
It shows up in the complete list
"""
tracker = TaskTracker()
task_1 = Task("Walk the dog")
taks_2 = Task("Walk the cat")
tracker.add(task_1)
tracker.add(task_2)
task_1.mark_complete()
tracker.list_complete() # => [task_1]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

