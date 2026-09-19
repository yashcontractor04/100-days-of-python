# Automated Email Birthday Wisher
An automated email dispatch system using Python's `smtplib`, `datetime`, and `pandas`. Cross-references a persistent tabular dataset of birthdays against the current date, personalizes a randomized template, and transmits an email greeting over a secure TLS SMTP transport layer.

### Tech / Concepts
* Transport Layer Security (TLS) and email dispatch via `smtplib`
* Temporal validation and matching via `datetime`
* Tabular filtering and record traversal using `pandas`
* Local configuration security via `python-dotenv` and environment variables

### Quickstart
1. Install dependencies:
   `pip install pandas python-dotenv`
2. Create your `.env` file:
   ```text
   MY_EMAIL=your_email@gmail.com
   PASSWORD=your_google_app_password
