def display_menu():
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task":task, "completed":False})
    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("no task in the list")
    else:
        print("\Tasks:")
        print("tasks",tasks)
        for i, task in enumerate(tasks,1):
            status =  "Completed" if task["completed"] else "Pending"
            print(f"{i}.{task['task']} - {status}")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("enter the task number to mark as complete"))
        tasks[task_number - 1]["completed"] = True
        print("Tak marked as completed")
    except(IndexError, ValueError):
        print("Invalid task number")

def remove_task(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to remove"))
        del tasks[task_number - 1]
        print("Tak removed successfully")
    except (IndexError, ValueError):
        print("Invalid Taks number")


#main function

def main():
    tasks = []
    while True:
        display_menu()
        choise = input("enter your choice (1-5): ")
        if choise == "1":
            add_task(tasks)
        elif choise == "2":
            view_tasks(tasks)
        elif choise == "3":
            mark_completed(tasks)
        elif choise == "4":
            remove_task == "4"
        elif choise == "5":
            print("exiting....")
            break
        else:
            print("invalid parameter please enter a number between 1 to 5")


if __name__ == "__main__":
    main()