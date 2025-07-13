tasks = []
def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['title']} [{status}]")
def add_task():
    title = input("Enter task:")
    tasks.append({"title": title, "done": False})
    print("Task added")
def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark as done:"))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except:
        print("Please enter a number")
def update_task():
    show_tasks()
    try:
        num = int(input("Enter task number to update"))
        if 1 <= num <= len(tasks):
            new_title = input("Enter new task name")
            tasks[num - 1]["title"] = new_title
            print("Task updated")
        else:
            print("Invalid task number")
    except:
        print("Please enter a number")
def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete"))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number")
    except:
        print("Please enter a number")
def main():
    while True:
        print("\nMenu:")
        print("1.Show Tasks")
        print("2.Add Task")
        print("3.Mark Task as Done")
        print("4.Update Task")
        print("5.Delete Task")
        print("6.Exit")
        choice = input("Choose an option:")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
main()
