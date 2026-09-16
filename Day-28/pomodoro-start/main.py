# ---------------------------- IMPORTS ------------------------------- #
import subprocess
from tkinter import *
import math
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- ALERTS ------------------------------- #
def play_alert(message):
    """Dispatches a macOS system audio alert, desktop banner, and focuses the window."""
    # Play system sound asynchronously using afplay
    subprocess.Popen(["afplay", "/System/Library/Sounds/Pop.aiff"])

    # Trigger native macOS notification banner via AppleScript
    script = f'display notification "{message}" with title "Pomodoro Timer"'
    subprocess.Popen(["osascript", "-e", script])

    # Bring application window temporarily to the foreground
    window.attributes("-topmost", 1)
    window.attributes("-topmost", 0)
    window.lift()

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Cancels running countdown cycle and clears the session state and UI."""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Determines active cycle stage (Work/Short Break/Long Break) and triggers countdown."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Every 8th cycle: 20-minute long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
        if reps > 1:
            play_alert("Time for a long break! Relax.")
    # Every even cycle: 5-minute short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Short Break", fg=PINK)
        if reps > 1:
            play_alert("Work session done! Take a 5-minute break.")
    # Every odd cycle: 25-minute work block
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
        if reps > 1:
            play_alert("Break is over! Time to get back to work.")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Recursively schedules UI second decrements via Tkinter event loop (window.after)."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Pad single-digit seconds with leading zero for digital clock formatting
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # Reschedule next frame tick after 1000 milliseconds (1 second)
        timer = window.after(1000, count_down, count - 1)
    else:
        # Transition to next stage when timer hits 0
        start_timer()
        # Compute completed work sessions (every full work block completes an even rep count)
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Header title
label_timer = Label(text="Timer", font=(FONT_NAME, 38), fg=GREEN, bg=YELLOW, pady=30)
label_timer.grid(row=0, column=1)

# Central graphic canvas with digital clock overlay
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Control buttons
start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

# Completed work block indicators
label_check = Label(text="", font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)

window.mainloop()