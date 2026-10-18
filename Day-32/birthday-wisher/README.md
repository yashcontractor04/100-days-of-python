# Day 32: Birthday Wisher

Sends birthday emails. Each time it runs, it looks in `birthdays.csv` for anyone whose birthday is today. For each person it picks one of 3 letter templates at random, puts their name in the letter and sends it with Gmail.

## Setup

1. `birthdays.csv` is not in the repo, because it would hold real names and email addresses (it is listed in `.gitignore`). To make your own, copy `dummy_birthdays.csv`, rename the copy to `birthdays.csv` and put in your own people. The columns are `name,email,year,month,day`.
2. Create a file called `.env` in this folder with your Gmail login:

   ```text
   MY_EMAIL=you@gmail.com
   MY_EMAIL_PASSWORD=your_gmail_app_password
   ```

   For the password, use a Gmail "app password" (a special password just for apps), not your normal one.
3. Run it with `python main.py`

## It also runs by itself

A GitHub Actions workflow (`.github/workflows/day_32_birthday_wisher.yml`) runs this script every day at 05:00 UTC. GitHub Actions is GitHub's tool for running code automatically. The email login and the birthday list are saved as "secrets" in the repository settings, so nobody can see them in the code.
