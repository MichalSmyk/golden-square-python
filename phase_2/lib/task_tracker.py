class TaskTracker():
    def __init__(self):
        self._tasks = []
         

    def add(self, task):
       self._tasks.append(task)

    def list_incomplete(self):
       return self._tasks

    def mark_complete(self, index):
        #Parameters:
        #   index: an integer representing thetask to complete
        #Side-effect:
        #   Removes the task at index from the list of tasks
        pass