
import io

tasks = [] # global variable. It is a list of dictionaries.

    """
    The next function reads tasks from a document and returns a task-list.

    Args:
    document_content (str): the content of the document to read tasks from.

    Returns:
    list: a task-list.
    """
def read_tasks_from_document(document_content):
    tasks = []
    for line in document_content.splitlines():
        task_details = line.split(": ", 1) # line.split has a second argument, which is the maximum number of splits to do. No splits in description. It splits at ':', is 1st argument..
        if len(task_details) == 2: # at the end of every task with description.
            task = {
                "title": task_details[0],
                "description": task_details[1],
            } # task is a dictionary with two keys, title and description.
            tasks.append(task) # append task to local list named tasks.
    return tasks
    """
    Loads tasks from a document and returns a list of tasks.

    Args:
    document_path (str): the path of the document to load tasks from.

    Returns:
    list: a task-list.
    """
def load_tasks_from_document(document_path):
    try:
        with io.open(document_path, 'r') as file: # opened to read.
            return read_tasks_from_document(file.read())
    except FileNotFoundError:
        return []
    """
    Saves tasks to a .txt file.

    Args:
    tasks (list): a task-list to save.
    document_path (str): the path of the file.
    """
def save_tasks_to_document(tasks, document_path):
    with io.open(document_path, 'w') as file: # opened to write.
        for task in tasks:
            file.write(f"{task['title']}: {task['description']}\n")
    """
    Adds a task to the task-list.

    Args:
    title (str): the title of the task.
    description (str): the description of the task.
    """
def add_task(title, description):
    task = {
        "title": title,
        "description": description,
    }
    tasks.append(task)
    save_tasks_to_document(tasks, "tasks.txt")
    """
    Prints the list of tasks.
    """
def view_tasks():
    for idx, task in enumerate(tasks): # enumerate returns a tuple with the index and the value of the item at that index.
        print(f"{idx + 1}. Title: {task['title']}") 
        print(f"   Description: {task['description']}")
        print("-" * 30)
    """
    Marks a task as completed.

    Args:
    task_index (int): the index of the task to mark as completed.
    """
def mark_completed(task_index):
    if 0 <= task_index < len(tasks): # if task_index is in the range of tasks. len(tasks) is the number of tasks.
        completed_task = tasks.pop(task_index) # pop removes the item at the given index and returns it.
        print(f"Task '{completed_task['title']}' marked as completed and removed from the task-list.")
        save_tasks_to_document(tasks, "tasks.txt")
    """
    Loads the initial tasks from the tasks.txt document.
    """
def load_initial_tasks():
    global tasks
    tasks = load_tasks_from_document("tasks.txt")

load_initial_tasks()

# This is the User Interface (UI) code
while True:
    print("Options:")
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Mark Task as Completed")
    print("4: Exit")

    choice = input("Enter your choice: ")

# This is were the arguments get hard coded into the functions.
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
        print("Ciao!")
        break
    else:
        print("Invalid choice. Please try again.")
    print("Thank you for using my Task manager! It means a lot to me that you chose to use my program today. Your tasks have been saved.")