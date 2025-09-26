
---

# 📄 `learning-journal.md`

# Learning Journal — Exercise 1.1

## What I set up
- Installed Python 3.8.7 on Windows and verified pip.
- Configured PATH so the correct Python is used.
- Installed and used `virtualenvwrapper-win` to manage environments.
- Created a virtual environment (`cf-python-base`).
- Built a simple script (`add.py`) that adds two numbers entered by the user.
- Installed IPython and explored its interactive shell.
- Generated a `requirements.txt` file using `pip freeze`.
- Created a second environment (`cf-python-copy`) and installed dependencies from `requirements.txt`.

## What I learned
- How to create and manage virtual environments on Windows using `workon` and `deactivate`.
- How to write and run a simple Python program from the command line.
- How to install packages into a virtual environment with pip.
- How to capture dependencies in `requirements.txt` and rebuild the same environment elsewhere.
- The importance of PATH order in Windows when working with multiple `python.exe` locations.

## What I want to learn next
- How to organize larger Python projects with multiple modules.
- How to write unit tests with `pytest`.
- How to use tools like `black` and `flake8` for consistent code style.
- How to publish projects to GitHub with a clean workflow.

# Learning Journal — Exercise 1.2 (Data Types)

**Date:** 9-26-2025  
**Topic:** Variables, data types, slicing, and basic data structures in Python

## What I accomplished
- Learned to use Python’s core data types: numbers, tuples, lists, strings, and dictionaries.  
- Completed five practice tasks covering type conversion, tuple slicing, list operations, string slicing, and dictionary creation with `zip()`.  
- Built Task 1.2: five recipe dictionaries combined into an `all_recipes` list and printed their ingredients.  
- Organized project with `all_recipes.py`, `README.md`, and a `screenshots/` folder.

## Key concepts I learned
- **Slicing:** start is inclusive, stop is exclusive (fixed my “awesome” off-by-one issue).  
- **Step slicing:** `s[::2]` gives even indices, `s[1::2]` gives odd ones.  
- **Mutability:** lists & dictionaries are mutable; tuples & strings are immutable.  
- **Data structures:** dictionaries work best for recipes (named fields), lists work best for collections of recipes.

## Challenges and solutions
- Tried `conda` but it wasn’t installed; switched to `virtualenvwrapper-win` (`workon cf-python-base`).  
- Got confused with slicing indexes; solved by mapping out index charts.  
- Learned how to clear the screen in both Command Prompt (`cls`) and IPython (`%clear`).


## Example code I’m proud of
```python
for recipe in all_recipes:
    print(recipe["name"], "ingredients:", recipe["ingredients"])
