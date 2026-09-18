# German-English Flashcard Memorization App
A desktop flashcard learning tool developed using Python's `tkinter` and `pandas`. Uses Leitner-style spaced card flipping with automatic progress persistence to prioritize unlearned vocabulary across sessions.

### Tech / Concepts
* Desktop interface architecture using `tkinter.Canvas` layer modifications
* State scheduling with `window.after()` and `window.after_cancel()`
* Tabular file ingestion and DataFrame mutation using `pandas`
* Defensive local caching (`try/except FileNotFoundError`) to track user learning progress

### Quickstart
1. Install requirements:
   `pip install pandas`
2. Run the application:
   `python main.py`
