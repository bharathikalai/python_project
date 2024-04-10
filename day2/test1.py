class Task:
    def __init__(self,description,completed=False):
        self.description = description
        self.completed = completed

description = "i go to temple"

task = Task(description)

print(task.description)
print(task.completed)