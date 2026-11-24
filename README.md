# Python ToDo CLI

A lightweight command-line task manager written in Python, featuring object-oriented design and CSV data persistence.

## Features
- **Add Tasks**: Store task names, descriptions, and priority levels.
- **Remove Tasks**: Delete completed tasks by their item number.
- **List Tasks**: View all active items in a formatted list.
- **Data Persistence**: Automatically reads and writes tasks to `todolist.csv` with UTF-8 encoding.
- **Validation**: Includes bounds checking and input validation to prevent invalid operations.

## Project Structure
- `todo.py`: Core application containing the `Task` and `ToDoList` classes, along with the interactive menu.
- `test_todo.py`: Automated unit tests covering task addition, deletion, validation, and CSV round-tripping.
- `.gitignore`: Excludes runtime files and local CSV storage from version control.

## Usage
Run the application directly with Python 3:
```bash
python todo.py
```

Run automated tests:
```bash
python -m unittest test_todo.py
```
