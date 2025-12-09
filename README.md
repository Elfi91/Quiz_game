# Project: Python Quiz Game 🧠
This project implements a simple quiz game (CLI - Command Line Interface) in Python. The main objective was the **Refactoring** of the code to reorganize it into logical **package** (`data` and `ui`), thereby improving the project's modularity, maintainability, and code stability.


## 📁 Package Structure
The code structure is organized into the following logical packages inside the root folder `QUIZ_GAME/`:

* **`main.py`**: The application's entry point, containing the **Control Flow Logic** (the master `while` loop) and the core business rule (`is_answer_correct`).

* **`data/`**: Contains the logic for file handlding and data preparation.
    * `repository.py`: **Repository Layer**. Handles low-level I/O (opening files) and access to the resource files.
    * `services.py`: **Service Layer**. Contains data manipulation logic, including reading the question index, extracting content, and the **`generate_statistics`** function.

* **`ui/`**: Contains all logic for user interaction.
    * `console.py`: Handles all I/O, including displaying questions, showing feedback, and validating user choice (`validate_choice`).

* **`questions_answers/`**: Folder containing the text resource files (index file and individual question files).


## 🚀 Requirements
To run this project, **Python 3.x** is required.


## ✅ Project Status and Architecture
### Current Status
The architectural refactoring is **100% complete** and the application is fully functional.

### Architectural Highlights
* **Separation of Concerns**: Functions are strictly separated into Data (I/O, Processing) and UI (Input/Output/Validation).
* **Robust Path Handling**: The project uses **`pathlib.Path`** to construct file paths, ensuring the application successfully finds the resource files (`questions_answers/`) regardless of the directory from which the script is executed.
