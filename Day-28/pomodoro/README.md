# Day 28: Pomodoro Timer

A Pomodoro timer in a small `tkinter` window (tkinter is Python's tool for making windows with buttons). The Pomodoro method means working in short blocks with breaks in between: 25 minutes of work, then a 5 minute break, and a 20 minute break after every fourth work block. A tick mark appears for each work block you finish. Start begins the timer and Reset stops it.

The alerts only work on a Mac. When a block ends, the program plays a sound and shows a notification using Mac-only commands (`afplay` and `osascript`). On Windows or Linux those commands don't exist, so you would get an error when the first block ends.

To run it: `python main.py`
