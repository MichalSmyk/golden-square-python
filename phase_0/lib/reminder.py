# File: lib/reminder.py

class Reminder:
    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        #add error 
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"