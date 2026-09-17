# ---------------------------- IMPORTS ------------------------------- #
import email
from pydoc import text
from re import search
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # Populate entry field and clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entries():
    """Validates inputs, then reads, appends, and writes credentials to data.json using defensive exception handling."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            # File does not exist or is empty/corrupt
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # File exists and contains valid JSON -> merge and save
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Save updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Searches data.json for a matching website key and displays stored credentials."""
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found.")
    else:
        if website in data.keys():
            messagebox.showinfo(title=website, message=f"Username: {data[website]['Username']}\nPassword: {data[website]['Password']}")
        else:
            messagebox.showerror("Error", "No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Central graphic canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Website row
website_label = Label(text="Website:", pady=5)
website_label.grid(row=1, column=0)
website_entry = Entry(width=21, highlightthickness=2)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=12)
search_button.grid(row=1, column=2)

# Email/Username row
username_label = Label(text="Email/Username:", pady=5)
username_label.grid(row=2, column=0)
username_entry = Entry(width=38, highlightthickness=1)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "yashcontractor04@gmail.com")

# Password row
password_label = Label(text="Password:", pady=5)
password_label.grid(row=3, column=0)
password_entry = Entry(width=21, highlightthickness=1)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(row=3, column=2)

# Action/Add button
add_button = Button(text="Add", width=36, command=save_entries)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()