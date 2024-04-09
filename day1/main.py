import os
def show_menu():
    print("simple to-do list")
    print("1. view tasks")
    print("2. Add task")
    print("3. mark task as completed")
    print("4.remove task")
    print("5.exist")

def view_tasks(tasks):
    if tasks:
        print("Tasks")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")
    else:
        print("No task")
def add_task(tasks):
    task = input("Enter task:")
    tasks.append(task)
    print("task added")

def mark_task_completed(tasks):
    view_tasks(tasks)

    if tasks:
        try:
            index = int(input("eneter the task number to masrk as completed")) -1
            tasks[index] += " (completed)"
            print("task marked as copleted")
        except (InterruptedError,ValueError,IndexError):
            print("invalid taks number")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("eneter task number to remove")) - 1
            del tasks[index]
            print("task removed")
        except(IndexError,ValueError):
            print("invalid task number")


def main():
    tasks  = []   #empty 
    filename = "/home/bharathibk/github/python_project/day1/tasks.txt"

    if os.path.exists(filename):
        with open(filename,"r") as file:
            tasks = [line.strip() for line in file]
    while True:
        show_menu()
        choice = input("enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            with open(filename,"w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print("good boy")
            break
        else:
            print("invalid choice please enter a number between 1 and 5")

if __name__ == "__main__":
    main()