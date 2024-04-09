def mark_task_completed(tasks):
    for i,task in enumerate(tasks,1):
        print(f"{i},{task}")

    try:
        index = int(input("enter task number to mark as completed: ")) - 1
        tasks[index] +="(completed)"
        print("task marked as completed")
    except(IndexError,ValueError):
        print("invalid task number")


#example usage
tasks = ["task1","task2","task3"]
while True:
    mark_task_completed(tasks)