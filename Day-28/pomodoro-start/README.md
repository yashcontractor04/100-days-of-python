# Desktop Pomodoro Productivity Timer
A desktop productivity application adhering to the Pomodoro Technique, developed using Python's `tkinter` GUI framework. Features recursive asynchronous timer callbacks, canvas graphic layering, and native macOS desktop notifications.

### Tech / Concepts
* `tkinter` event-loop asynchronous scheduling via `window.after()` and `window.after_cancel()`
* Multi-layer GUI rendering using `tkinter.Canvas` (`PhotoImage`, text items)
* Modulo-based state machine tracking work/break stage transitions
* Native macOS system integration via `subprocess`

### Quickstart
`python main.py`
