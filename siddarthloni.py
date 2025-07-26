#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To-Do List Manager
# Created by Siddarth Loni
# Mini Project for Internship - June 2025

import json
import os
from datetime import datetime, timedelta

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Load tasks when the program starts
tasks = load_tasks()

# Add a new task
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) [press Enter to skip]: ")
    priority = input("Enter priority (low/medium/high) [default: medium]: ") or "medium"
    task = {
        "description": description,
        "due_date": due_date if due_date else None,
        "status": "pending",
        "priority": priority.lower()
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# View tasks with filters
def view_tasks():
    print("\n--- View Tasks ---")
    print("1. View All Tasks")
    print("2. View Completed Tasks")
    print("3. View Pending Tasks")
    print("4. View Tasks Due Soon (within 3 days)")
    choice = input("Choose an option: ")

    now = datetime.now()
    for i, task in enumerate(tasks, start=1):
        due = task['due_date']
        due_str = f" | Due: {due}" if due else ""
        info = f"{i}. {task['description']} [Status: {task['status'].capitalize()} | Priority: {task.get('priority', 'medium').capitalize()}]{due_str}"

        if choice == '1':
            print(info)
        elif choice == '2' and task['status'] == 'completed':
            print(info)
        elif choice == '3' and task['status'] == 'pending':
            print(info)
        elif choice == '4' and due:
            try:
                due_date = datetime.strptime(due, '%Y-%m-%d')
                if 0 <= (due_date - now).days <= 3:
                    print(info)
            except ValueError:
                print(f"Invalid date format for task: {task['description']}")

# Mark a task as completed
def mark_task_completed():
    print("\n--- Mark Task as Completed ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']} [Status: {task['status']}]")

    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['status'] = 'completed'
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Edit an existing task
def edit_task():
    print("\n--- Edit Task ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']}")

    try:
        index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_description = input("Enter new description (leave blank to keep current): ")
            new_due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ")
            if new_description:
                tasks[index]['description'] = new_description
            if new_due_date:
                tasks[index]['due_date'] = new_due_date
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    print("\n--- Delete Task ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']}")

    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def menu():
    while True:
        print("\n========= TO-DO LIST MANAGER =========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    menu()


# In[ ]:




