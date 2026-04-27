# Simple Task Tracker

## Overview

This is a simple Task Tracker project made with Python. It helps users manage daily tasks using a menu-driven program. Users can add tasks, view all tasks, delete tasks, and update task priority.

The project also uses a JSON file to save tasks, so the data stays saved even after closing the program.

---

## Features

* Add a new task
* View all tasks
* Delete a task
* Update task priority
* Save tasks in JSON file
* Load saved tasks when program starts

---

## Task Structure

Each task is stored like this:

```python id="a2f49k"
{
    "title": "Study python",
    "description": "Finish loops",
    "priority": "High"
}
```

---

## Menu

```text id="yd8q7s"
===== Task Tracker =====
1. Add Task
2. View Tasks
3. Delete Task
4. Update Task Priority
5. Exit
```

---

## Priority Levels

The program uses three priority levels:

* High
* Medium
* Low

---

## Concepts Used

* Python Class and Object
* Functions / Methods
* List and Dictionary
* Loop
* If-Else Condition
* JSON File Handling
* Exception Handling

---

## How It Works

1. Program starts and loads tasks from `tasks.json`
2. User selects an option from menu
3. Tasks can be added, viewed, deleted, or updated
4. Changes are saved automatically

---

## Conclusion

This project helped me practice Python basics, object-oriented programming, and file handling. It is a useful beginner project for learning how real programs store and manage data.
