# Day 10: Calculator

A calculator for the terminal. Pick `+`, `-`, `*` or `/`, type two numbers and you get the answer. After that you can type `y` to keep going with the answer, `n` to start a new calculation, or `e` to quit.

Instead of a long chain of `if` statements, the symbols are stored in a dictionary that points to the matching function (for example `+` points to `add`).

Dividing by zero isn't handled, so the program crashes if you try it.

To run it: `python main.py`
