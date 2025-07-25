import datetime
import json
import os
import sys

# Utility functions
def read_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def write_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

# Operations
def add_task(description):
    tasks = read_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    write_tasks(tasks)
    print(f"Task added successfully (ID {task_id})")

def update_task(task_id, new_description):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    if task:
        task["description"] = new_description
        task["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_tasks(tasks)
        print(f"Task {task_id} updated successfully")
    else:
        print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)
        write_tasks(tasks)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task {task_id} not found")

def mark_task(task_id, status):
    tasks = read_tasks()
    task = find_task(tasks, task_id)
    if task:
        task["status"] = status
        task["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_tasks(tasks)
        print(f"Task {task_id} marked as {status}")
    else:
        print(f"Task {task_id} not found")

def list_tasks(status=None):
    tasks = read_tasks()
    if not tasks:
        print("No tasks found")
        return
    for i, task in enumerate(tasks, 1):
        if not status or task["status"] == status:
            print(f"Task {i}")
            print(f"  ID: {task['id']}")
            print(f"  Description: {task['description']}")
            print(f"  Status: {task['status']}")
            print(f"  Created At: {task['created_at']}")
            if "updated_at" in task:
                print(f"  Updated At: {task['updated_at']}")
            print("-" * 40)

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: task_tracker.py <command> [args...]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Invalid command or missing arguments")

if __name__ == "__main__":
    main()