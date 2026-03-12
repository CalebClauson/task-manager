# Python Task List CLI

## Overview

This is a simple command line task manager I developed as a beginner project while learning Python.

The program allows users to manage tasks directly from the terminal while storing them in a text file so the data persists between program runs.

## Purpose

This project was created as part of my early learning in Python to practice working with loops, file handling, list manipulation, and input validation while building a small command line utility.

## Features

### View Tasks

Displays all tasks currently stored in the task file.

Completed tasks are marked and displayed in green to make them easier to identify.

Example:

1. Buy groceries  
2. [✓] Clean room  
3. Finish homework  

### Add Task

Allows the user to enter a new task which is appended to the task list file.

Example:

Buy groceries

### Edit Task

Allows a user to modify an existing task by selecting its line number.

Completed tasks cannot be edited to prevent accidental modification.

### Complete Task

Marks a task as completed by adding a completion marker to the beginning of the task.

Example:

[✓] Clean room

Completed tasks are also displayed in green when viewed in the terminal.

### Delete Task

Removes a selected task from the task list entirely.

## What I Learned

This project helped me practice:

* Reading and writing files in Python
* Working with lists and indexes
* Input validation and error handling
* Loop control using `continue` and `return`
* Structuring programs into multiple functions
* Improving command line user interaction

It also helped reinforce the pattern of:

```
read → modify → write
```

which is commonly used when manipulating data stored in files.

## Project Structure

TaskList/

* main.py
* task.py
* tasks.txt
* README.md

## How to Run

1. Navigate to the project directory.

2. Run the program:

```
python3 main.py
```

3. Follow the prompts to view, add, edit, complete, or delete tasks.

## Requirements

* Python 3.x
* No external libraries required

## Future Improvements

Possible future improvements include:

* Task priorities
* Due dates
* Sorting tasks
* Better command line formatting
* Saving completed tasks separately
* Adding a graphical interface