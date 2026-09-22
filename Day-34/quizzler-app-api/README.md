# Quizzler Desktop GUI Quiz App
A desktop trivia application built with Python's `tkinter` and Open Trivia DB API. Consumes REST endpoints dynamically based on user category and question-count configurations, unescapes HTML character entities, and delivers interactive visual feedback.

### Tech / Concepts
* Dynamic API parameter querying using `requests`
* HTML entity decoding with Python's standard `html.unescape`
* Desktop UI rendering with `tkinter` dialogs, Canvas card layout, and `after()` state transitions
* Strict UI interaction gating (disabling buttons during feedback delays)

### Quickstart
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the application:
   `python main.py`
