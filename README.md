# Simple Task Tracker

## Overview

This project is a minimal yet structured implementation of a command-line Task Tracker built using Python. The primary goal of this application is to demonstrate a clear understanding of object-oriented programming principles, basic data structures, and persistent storage using JSON.

The program allows users to manage daily tasks through a simple interface, supporting the addition, viewing, and deletion of tasks. Despite its simplicity, the design emphasizes clean structure, logical flow, and data persistence.

---

## Features

* Add new tasks with a title and description
* View all existing tasks in an organized format
* Delete tasks using indexed selection
* Persistent storage using a JSON file

---

## Technical Approach

### Data Representation

Tasks are stored as dictionaries containing two fields:

* `title`
* `description`

All tasks are maintained within a list, which acts as the primary in-memory data structure.

---

### Object-Oriented Design

The program is structured around a single class, `TaskManager`, which encapsulates:

* Task storage (`self.tasks`)
* Core operations (add, view, delete)
* File handling (load and save)

This approach ensures that both data and behavior are logically grouped, improving readability and maintainability.

---

### Persistence Mechanism

To ensure that tasks are not lost between program executions, the application uses a JSON file (`tasks.json`) as a storage medium.

* On startup, the program attempts to load existing tasks from the file
* After any modification (add/delete), the updated list is written back to the file

This creates a simple but effective persistence layer without introducing database complexity.

---

## Program Flow

1. The program initializes and loads existing tasks (if available)
2. A menu-driven loop allows continuous user interaction
3. Based on user input:

   * Tasks can be added, viewed, or deleted
4. The loop continues until the user explicitly exits

---

## Limitations

* No advanced input validation for all edge cases
* No support for editing or marking tasks as complete
* Not optimized for large-scale data handling

These limitations are intentional to maintain focus on core programming concepts.

---

## Possible Improvements

* Add task status (completed/pending)
* Implement editing functionality
* Improve input validation and error handling
* Replace JSON storage with a database for scalability

---

## Conclusion

This project reflects a foundational understanding of Python programming, particularly in structuring programs using classes and managing data effectively. While simple in scope, it provides a solid base for extending into more complex task management systems.

