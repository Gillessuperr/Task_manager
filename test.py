import io

tasks = []

def read_tasks_from_document(document_content):
    tasks = []
    for line in document_content.splitlines():
        task_details = line.split(": ", 1)
        if len(task_details) == 2:
            task = {
                "title": task_details[0],
                "description": task_details[1],
            }
            tasks.append(task)
    return tasks

def load_tasks_from_document(document_path):
    try:
        with io.open(document_path, 'r') as file:
            return read_tasks_from_document(file.read())
    except FileNotFoundError:
        return []

def save_tasks_to_document(tasks, document_path):
    with io.open(document_path, 'w') as file:
        for task in tasks:
            file.write(f"{task['title']}: {task['description']}\n")

def add_task(title, description):
    task = {
        "title": title,
        "description": description,
    }
    tasks.append(task)
    save_tasks_to_document(tasks, "tasks.txt")

def view_tasks():
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print("-" * 30)

def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        print(f"Task '{completed_task['title']}' marked as completed and removed from the task-list.")
        save_tasks_to_document(tasks, "tasks.txt")

def load_initial_tasks():
    global tasks
    tasks = load_tasks_from_document("tasks.txt")

load_initial_tasks()

while True:
    print("Options:")
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Mark Task as Completed")
    print("4: Exit")

    choice = input("Enter choice (1, 2, 3, or 4): ")

    if choice == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        mark_completed(task_index)
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid option (1, 2, 3, or 4).")