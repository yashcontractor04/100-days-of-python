# Day 50: Auto Swiping Bot

Automates swiping right on TinDog (a Tinder clone mock platform). It opens Chrome using Selenium, logs into the app using a social popup login window, accepts initial web permissions, and repeatedly clicks the like button.

It handles popups that appear when a match occurs (`ElementClickInterceptedException`) and pauses if elements take longer to load (`NoSuchElementException`).

## Setup

Create a file called `.env` in this folder:

```text
EMAIL=your_email
PASSWORD=your_password
```
To run it: `python main.py`