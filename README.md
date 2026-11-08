# Los Pollos Hotel Management System

A command-line hotel management project written in Python for a Class XII Computer Science project. It uses MySQL to store room and customer records and the `tabulate` package to format terminal output.

## Requirements

- Python 3
- MySQL Server
- Python packages: `mysql-connector-python` and `tabulate`

Install the Python packages with:

```powershell
python -m pip install mysql-connector-python tabulate
```

## Setup and run

1. Start a local MySQL server.
2. Review the connection settings near the top of `CS PROJECT_XII PROJECT.py` and set them to match your local MySQL account. Do not use real credentials in a public commit.
3. Run the program:

```powershell
python "CS PROJECT_XII PROJECT.py"
```

The script creates and uses a `los_pollos` database and its tables. Run it only against a development database you are comfortable changing.

## Project context

Created as a school project by Fahad, Vishnupriyan, and Malif. This repository preserves the original educational project.
