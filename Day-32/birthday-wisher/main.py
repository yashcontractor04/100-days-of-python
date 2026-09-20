import datetime as dt
import os
import smtplib
import random
import pandas as pd
from dotenv import load_dotenv
##################### Extra Hard Starting Project ######################

# Load sensitive environment credentials from .env file
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# Determine current calendar day
today = (dt.datetime.now().month, dt.datetime.now().day)

# Ingest birthday data
data = pd.read_csv('birthdays.csv')

# Map (month, day) tuple to a list of matching records to handle multiple birthdays on the same day
matches = data[(data["month"] == today[0]) & (data["day"] == today[1])]

# Process matches and dispatch personalized emails
if not matches.empty:
    for _, person in matches.iterrows():
        # Select random letter
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

        with open(file_path) as letter:
            contents = letter.read()
            personalized_letter = contents.replace("[NAME]", person["name"].strip())

        # Construct email headers and payload
        subject = "Happy Birthday!"
        email_message = f"From: {MY_EMAIL}\r\nTo: {person['email']}\r\nSubject: {subject}\r\n\r\n{personalized_letter}"

        # Transmit via secure SMTP connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            # Upgrade connection to secure TLS encryption
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person["email"], msg=email_message.encode("utf-8"))
            print(f"Birthday greeting successfully dispatched to {person['name']}.")

else:
    print("No birthdays registered for today.")
