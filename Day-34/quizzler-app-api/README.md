# Day 34: Quizzler

A true/false quiz app in a `tkinter` window. When it starts, it asks how many questions you want (1 to 50) and which category: `science` (Science: Computers) or `general` (General Knowledge). Then it gets the questions from the Open Trivia Database website. You don't need a key for it. The question card turns green when you are right and red when you are wrong.

- `data.py`: gets the questions from the website
- `question_model.py` and `quiz_brain.py`: store the questions and keep track of progress and score
- `ui.py`: the window

The website sends some characters in a special code (for example `&quot;` instead of a quote mark). `quiz_brain.py` turns them back into normal text with `html.unescape`. The `images` folder has the pictures for the true and false buttons.

You need an internet connection. To run it: `python main.py`
