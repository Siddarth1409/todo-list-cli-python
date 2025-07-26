# To-Do List Manager

This is a console-based Python application that allows users to manage their daily tasks efficiently. Tasks can be added, edited, viewed, marked as completed, or deleted. All task data is stored persistently using a JSON file.

## Features

- Add new tasks with optional due date and priority
- View all tasks, completed tasks, pending tasks, or tasks due within 3 days
- Mark tasks as completed
- Edit task description and due date
- Delete tasks
- Automatically saves all tasks to a local JSON file

## Technologies Used

- Python (Standard Library only)
- JSON for task data persistence
- datetime module for date comparison

## File Structure

```
to-do-list-manager/
├── tasks.json        # Stores the list of tasks
├── todo.py            # Main script for task management
└── README.md          # Project documentation
```

## How to Run

1. Ensure Python is installed on your system.
2. Download or clone this repository.
3. Navigate to the project directory.
4. Run the script using:
   ```bash
   python todo.py
   ```

## Sample Usage

1. Add a task: enter description, due date (optional), and priority (default is medium)
2. View tasks: choose to list all, completed, pending, or due soon
3. Edit or delete tasks based on the displayed task number
4. All changes are saved to `tasks.json`

## Author

Siddarth Loni
