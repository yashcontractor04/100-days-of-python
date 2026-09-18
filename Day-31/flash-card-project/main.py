import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA INITIALIZATION ------------------------------- #
# Attempt to load user's progress; fallback to source vocabulary dataset
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/deutsch_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

flip_timer = None
current_card = {}

# ---------------------------- CARD MECHANICS ------------------------------- #
def next_card():
    """Draws a random card, displays the front (German), disables buttons, and schedules the 3-second flip timer."""
    global current_card, flip_timer

    # Cancel pending flip callback if the user moves early
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # Check if the user has mastered all words in the deck

    if not to_learn:
        flashcard.itemconfig(card_side, image=card_front)
        flashcard.itemconfig(card_title, text="Completed!", fill="black")
        flashcard.itemconfig(card_word, text="All words learned!", fill="black")
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")
        return

    # Disable choice buttons while the front card is active
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")

    current_card = random.choice(to_learn)
    flashcard.itemconfig(card_side, image=card_front)
    flashcard.itemconfig(card_title, text="Deutsch", fill="black")
    flashcard.itemconfig(card_word, text=current_card["deutsch"], fill="black")

    # Schedule card flip to English after 3000 ms
    flip_timer = window.after(3000, flash)


def flash():
    """Flips the card to display the back face (English) and enables choice buttons."""
    flashcard.itemconfig(card_side, image=card_back)
    flashcard.itemconfig(card_title, text="English", fill="white")
    flashcard.itemconfig(card_word, text=current_card["english"], fill="white")

    right_button.config(state="normal")
    wrong_button.config(state="normal")


def is_known():
    """Removes the memorized word from the pool, serializes the updated list to CSV, and draws the next card."""
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("flashy")
window.config(width=1000, height=626, bg=BACKGROUND_COLOR, padx=50, pady=50)

# Asset loading
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# Card canvas
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = flashcard.create_image(0, 0, image=card_front, anchor="nw")
card_title = flashcard.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = flashcard.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
flashcard.grid(row=0, column=0, columnspan=2)

# Action controls
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=1)

# Start application flow
next_card()

window.mainloop()
