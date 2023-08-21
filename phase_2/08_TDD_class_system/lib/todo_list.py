class TodoList:
    def __init__(self):
        self._todo = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        return self._todo.append(todo)
        

    def incomplete(self):
        return [todo for todo in self._todo if not todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [todo for todo in self._todo if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass
