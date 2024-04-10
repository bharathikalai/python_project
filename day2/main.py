class Task:
    def __init__(self,description,completed= False):
        self.description = description
        self.completed = completed
    
    def mark_as_completed(self):
        self.completed = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,description):
        task = Task(description)
        self.tasks.append(task)


    def display_tasks(self):
        if not self.tasks:
            print("no task found")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(task,"task")
                status = "yes" if task.completed else "no"
                print(f"{index}.[{status}] {task.description}")

    def mark_task_as_completed(self,task_index):
        try:
            task = self.tasks[task_index - 1]
            task.mark_as_completed()
            print(f"Task '{task.description}' marked as completed ")
        except(IndexError,ValueError):
            print("INvalid task index")


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Mark task as Completed")
        print("4. Exit")
        choice = input("enter your choice   :")

        if choice == "1":
            description =  input("Enter task description   :")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("enter the index of task to mark as completed"))
            todo_list.mark_task_as_completed(task_index)
        elif choice == "4":
            print("Exiting..")
            break
        else:
            print("invalid choice please try again")
if __name__ =="__main__":
    main()
