class Task:
    def __init__(self,description):
        self.description = description
        self.next = None
class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self,description):
        new_task = Task(description)
        new_task.next = self.head
        self.head = new_task

    def view_tasks(self):
        current_task = self.head
        while current_task:
            print("task",current_task.description)
            current_task = current_task.next

task_manager = TaskManager()
task_manager.add_task("task1"
                      )
task_manager.add_task("task2"
                      )
task_manager.view_tasks()