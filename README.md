# Simple Task Tracker

## Project Overview

This project is a command-line Task Tracker developed in Python with a focus on clean software design, modularity, and persistent data management. It provides users with a lightweight system for organizing daily tasks while demonstrating practical application of core computer science concepts such as object-oriented programming, structured data modeling, file persistence, and user-driven control flow.

Although intentionally simple in scope, the project was designed with scalability and maintainability in mind. The architecture allows additional features to be integrated with minimal structural changes.

---

## Core Features

* Add tasks with custom titles and descriptions
* View all tasks in a structured numbered format
* Delete tasks by selecting task index
* Mark tasks as completed
* Persist task data using JSON storage
* Automatically restore saved tasks on program startup

---

## Data Model

Each task is represented as a structured dictionary containing descriptive metadata and completion state:

```python id="qu16hz"
{
    "title": "Study Python",
    "description": "Complete OOP module",
    "completed": False
}
```

Tasks are maintained in-memory as a list of dictionaries, providing efficient sequential access and straightforward serialization.

---

## System Design

## Object-Oriented Architecture

The application is centered around a `TaskManager` class responsible for encapsulating both state and behavior.

Responsibilities include:

* Maintaining task state (`self.tasks`)
* Handling task operations
* Managing persistent storage
* Running the interactive menu system

This class-based design improves cohesion, readability, and future extensibility.

---

## Persistence Layer

Rather than relying solely on runtime memory, the project implements a lightweight persistence mechanism through JSON.

### Workflow:

* On launch, previously saved tasks are loaded from `tasks.json`
* Any state-changing operation updates the file immediately
* User progress remains available across sessions

This approach provides a practical alternative to database integration for small-scale applications.

---

## User Interface Flow

```text id="v6i4ru"
===== Task Tracker =====
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Exit
```

The interface is intentionally minimal, emphasizing usability, predictable navigation, and low cognitive overhead.

---

## Example Output

```text id="37mwbj"
1. Study Python - Finish loops [Completed]
2. Exercise - 30 minutes walk [Not Completed]
3. Assignment - Submit Assignment [Not Completed]
```

---

## Technical Concepts Demonstrated

* Object-Oriented Programming (Classes, Methods, Encapsulation)
* Python Data Structures (Lists, Dictionaries)
* File Handling
* JSON Serialization / Deserialization
* Input Validation
* Conditional Logic
* Iteration and Control Flow
* Exception Handling

---

## Engineering Considerations

Several design decisions were made to improve reliability and maintainability:

* Separation of concerns between storage, logic, and interface
* Immediate persistence after state mutation
* Readable and modular method design
* Graceful handling of missing storage files
* Expandable architecture for future features

---

## Potential Extensions

Future versions of the project could include:

* Task editing functionality
* Priority levels and deadlines
* Search and filtering
* Completed / pending task views
* Data analytics (completion rate, productivity trends)
* GUI implementation using Tkinter or PyQt
* Database migration using SQLite or PostgreSQL
* Multi-user authentication system

---

## Why This Project Matters

While simple at the surface level, this project reflects the same foundational engineering patterns used in larger production systems:

* persistent state management
* modular design
* user interaction loops
* CRUD-style operations
* maintainable code organization

It serves as an effective demonstration of translating programming fundamentals into a functional software product.

---

## Conclusion

This Task Tracker represents more than a beginner exercise—it is a compact example of disciplined software development using Python fundamentals. By combining practical functionality with clean architecture, the project establishes a strong foundation for progression into larger application development and backend systems engineering.

