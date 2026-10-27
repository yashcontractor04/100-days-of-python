# Day 47: Amazon Price Tracker

Monitors the price of an item on Amazon (currently a Yum Asia rice cooker on Amazon Germany). It uses BeautifulSoup to scrape the product title and current price. If the price falls below €150.00, it sends an email alert via Gmail using `smtplib`.

Amazon blocks requests from standard scripts, so custom browser headers are passed with `requests` to get the page content.

## Setup

Create a file called `.env` in this folder:

```text
MY_EMAIL=you@gmail.com
SMTP_PASSWORD=your_gmail_app_password
TO_EMAIL=receiver@example.com
```
To run it: `python main.py`