import os
import json
from datetime import datetime

DATA_FILE = 'todo_data.json'

# Load data from JSON file if it exists, otherwise initialize empty lists
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'user1': [], 'user2': []}

# Save data to JSON file (only called at exit)
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Add task (saved in memory)
def add_task(user, data):
    task_description = input("Enter your task: ").strip()
    task = {
        "description": task_description,
        "status": "Not Done",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data[user].append(task)
    print("Task added successfully (not yet saved to file).")

# Display all tasks
def list_tasks(user, data):
    tasks = data.get(user, [])
    if not tasks:
        print("No tasks found.")
        return

    print(f"\nTasks for {user}:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']}")
        print(f"   Status : {task['status']}")
        print(f"   Created: {task['created']}")

# Mark task as completed
def mark_task_complete(user, data):
    tasks = data.get(user, [])
    if not tasks:
        print("No tasks to mark.")
        return

    list_tasks(user, data)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            data[user][task_num - 1]['status'] = 'Done'
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(user, data):
    tasks = data.get(user, [])
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks(user, data)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = data[user].pop(task_num - 1)
            print(f"Deleted task: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main app logic
def main():
    data = load_data()
    user = input("Enter your username (user1/user2): ").strip()
    if user not in ['user1', 'user2']:
        print("Invalid user.")
        return

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit and Save")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task(user, data)
        elif choice == '2':
            list_tasks(user, data)
        elif choice == '3':
            mark_task_complete(user, data)
        elif choice == '4':
            delete_task(user, data)
        elif choice == '5':
            save_data(data)
            print("Goodbye! All changes saved to", DATA_FILE)
            break
        else:
            print("Invalid option. Try again.")

# Run the app
if __name__ == "__main__":
    main()
