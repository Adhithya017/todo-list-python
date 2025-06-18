FILEPATH = "tasks.txt"

def get_tasks(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    return tasks

def write_tasks(tasks, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(tasks)

def show_menu():
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            tasks = get_tasks()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")

        elif choice == '2':
            task = input("Enter new task: ") + "\n"
            tasks = get_tasks()
            tasks.append(task)
            write_tasks(tasks)
            print("Task added!")

        elif choice == '3':
            tasks = get_tasks()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
            index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] = tasks[index].strip() + " ✔\n"
                write_tasks(tasks)
                print("Task marked as complete!")
            else:
                print("Invalid index!")

        elif choice == '4':
            tasks = get_tasks()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                write_tasks(tasks)
                print("Task deleted!")
            else:
                print("Invalid index!")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
