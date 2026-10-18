# Day 29: Password Manager

A small `tkinter` app for making and saving passwords.

- **Generate Password** makes a random password (a mix of letters, numbers and symbols) and copies it so you can paste it.
- **Add** saves the website, email and password in a file called `data.json`.
- **Search** looks up a website and shows the email and password saved for it.

The passwords are saved as plain text with no encryption, so this is only a practice project. Don't use it for real passwords. `data.json` is listed in `.gitignore`, so it never gets uploaded to GitHub.

The email box is filled in automatically with my email address. To change it, edit the line with `username_entry.insert` in `main.py`.

To run it: `python main.py`
