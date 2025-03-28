# Technical Lesson: PyPi, Pip & Python Scripting

## Learning Goals

- Use `pip` to install and manage Python packages from PyPi.
- Create and execute standalone Python scripts from the command line.
- Manage dependencies with `requirements.txt` or `Pipfile`.
- Automate repeatable processes using modular scripting.

## Introduction

In Python, scripting and package management are essential for building real-world tools and automation workflows. This lesson will cover:

- Installing packages with `pip` and tracking them with `requirements.txt`.
- Writing modular scripts using built-in or external packages.
- Structuring scripts to be reusable and executable from the command line.

Let’s consider an automation tool that generates a daily CSV report for a content team. The current system supports:

- Running manual scripts to generate reports.
- Using standard libraries like `datetime` and `csv`.

However, it lacks:

- Automated setup of required dependencies.
- Reproducible behavior across different machines.
- Clean project structure for scripting.

To address these gaps, we will:

1. Create a modular Python script that generates reports.  
2. Install and track external dependencies using `pip`.  
3. Use `requirements.txt` or `Pipfile` to ensure consistency.  
4. Structure scripts to be executable from the command line.

## Code Along

### Setting Up the Project

To get started, clone the repository and install any required dependencies.

If you're using `pipenv`:

```bash
git clone <repo-url>
cd course-7-module-6-pypi-pip-and-scripting-technical-lesson
pipenv install
```

Or, if you're using `pip` directly:

```bash
git clone <repo-url>
cd course-7-module-6-pypi-pip-and-scripting-technical-lesson
pip install -r requirements.txt
```

### Writing the Report Generator Script

We’ll modularize the logic into a file called `report_generator.py` and call it from a main script.

#### Example: `report_generator.py`

```python
# lib/report_generator.py

def generate_csv_report():
    # TODO: Write code to create and save a report CSV file
    pass
```

#### Example: `generate_report.py`

```python
# generate_report.py

from lib.report_generator import generate_csv_report

if __name__ == "__main__":
    # TODO: Call the function to generate the report
    pass
```

### Installing and Tracking Dependencies

To add an external dependency such as `requests`:

```bash
pip install requests
pip freeze > requirements.txt
```

Or with pipenv:

```bash
pipenv install requests
```

This ensures that collaborators can install the same dependencies with:

```bash
pip install -r requirements.txt
```

or

```bash
pipenv install
```

### Running the Script

To run the report generator:

```bash
python generate_report.py
```

Make sure `if __name__ == "__main__":` is used so the script runs properly from the CLI.

## Best Practices for Python Scripting

- Use `requirements.txt` or `Pipfile` to ensure environments are reproducible.  
- Isolate logic into modules (`lib/`, `src/`) and import where needed.  
- Use `__name__ == "__main__"` to control execution.  
- Comment and document clearly for maintainability.  
- Use virtual environments to avoid system-wide package conflicts.

## Conclusion

By mastering `pip`, PyPi, and scripting workflows, developers can:

- Automate tasks using reusable Python scripts.  
- Track and manage dependencies cleanly.  
- Create scalable, modular tools that run across different systems.  
- Collaborate more effectively through structured, reproducible environments.

These techniques are critical for building real-world backend utilities, developer tools, and automation pipelines in Python.
