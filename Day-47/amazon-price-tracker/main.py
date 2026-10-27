import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Credentials
MY_EMAIL = os.getenv("MY_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Cleaned URL
URL = "https://www.amazon.de/dp/B0B431NHJ1"
TARGET_PRICE = 150.00

# Custom browser headers, to avoid Amazon blocking out Python requests script
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}

# Getting page data
response = requests.get(URL, headers=headers)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

# Extract and clean whitespaces from product title
product_title = " ".join(soup.find(name='span', id='productTitle').get_text(strip=True).split())

# Parse whole and fraction parts of the price
price_whole = int(soup.find('span', class_='a-price-whole').get_text().split(".")[0].split(",")[0])
price_fraction = int(soup.find('span', class_='a-price-fraction').get_text())

total_price = price_whole + price_fraction / 100

print(f"{product_title} for €{total_price}")

# Send email if current price is below target price
if total_price < TARGET_PRICE:
    message = (f"Subject:Amazon Price Alert!\n\n"
               f"{product_title} is now available for €{total_price}.\n"
               f"{URL}")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=SMTP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=message.encode('utf-8'))
    print("Email alert for price change sent successfully.")