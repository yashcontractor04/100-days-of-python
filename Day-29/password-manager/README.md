# Desktop GUI Password Manager & Generator
A desktop password manager built with Python's `tkinter` interface toolkit. Features dynamic random password creation with system clipboard integration, structured JSON persistence, and defensive exception handling (`try`/`except`/`else`/`finally`) for data querying and updates.

### Tech / Concepts
* Desktop GUI architecture with `tkinter` (Grid layout manager, Dialogs, Canvas)
* Structured key-value disk persistence using the `json` module (`load`, `dump`, `update`)
* Defensive file handling with `try`/`except`/`else`/`finally` blocks
* System clipboard management via `pyperclip`

### Quickstart
1. Install dependencies:
   `pip install pyperclip`
2. Run the application:
   `python main.py`
