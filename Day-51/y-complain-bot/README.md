# Day 51: Internet Speed Complaint Bot

Automates testing your internet speed and posting a complaint if your provider isn't delivering what you pay for. It uses Selenium to visit Speedtest.net, clicks start, and reads the download and upload results.

If either speed is below your promised limits, it opens Y (a X, formerly Twitter, clone app), logs into your account, and posts a complaint message with your current speeds.

## Setup

Create a file called `.env` in this folder:

```text
Y_USERNAME=your_email
Y_PASSWORD=your_password
```
To run it: `python main.py`