# Project: Python Quiz Game 🧠
This project implements a simple quiz game (CLI - Command Line Interface) in Python. The main objective was the **Refactoring** of the code to reorganize it into logical **package** (`data` and `ui`), thereby improving the project's modularity and maintainability.

---

### 📁 Package Structure
The code structure is organized into the following logical packages inside the root folder `QUIZ_GAME/`:

* **`main.py`**: The entry point and core logic for quiz execution (`while` loop, navigation management, and final statistics calculation).

* **`data/`**: Contains the logic for data access and manipulation.
    * `repository.py`: **Repository Layer**. Low-level interface for I/O (opening and reading text files).
    * `services.py`: **Service Layer**. Business logic for transforming raw data into usable models (fetching the list of questions, extracting question/answer content).
* **`ui/`**: Contains the user interface logic.
    * `console.py`: Functions dedicated to displaying questions, feedback, and the quiz status (console output).
* **`questions_answers/`**: Folder containing the text resource files (the index file and the individual questions/answers).

---

## 🚀 Requirements

To run this project, **Python 3.x** is required.
---

## 🚩 Status and Next Steps

### Current Status
The package structure (`data/`, `ui/`, `questions_answers/`) has been correctly **created** in the `QUIZ_GAME/` root folder.

### Next Steps
**Copy Functional Code:** Insert the Python code into the respective modules (`repository.py`, `services.py`, `console.py`).
**Internal Imports Correction:** Update the import in `data/services.py` (from a relative import to `repository`).
**High-Level Imports Correction:** Update all imports in `main.py` to correctly point to the new packages (`data.services` and `ui.console`).
**Path Correction:** Update the path strings in the code to reflect the new location of the `questions_answers/` folder.