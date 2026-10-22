# 100 Days of Python

My solutions to the projects from Angela Yu's [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) on Udemy. I'm using the course to learn the Python I need for backend development.

Every project has its own folder with a README that explains what it does and how to run it.

## A few to look at first

- [Day 36, Stock News Alert](Day-36/stock-news): checks how much a stock moved in a day and sends news about it to Telegram if the move is big. It runs by itself on GitHub Actions, and the API keys are kept secret.
- [Day 40, Flight Club](Day-40/flight-club): looks for cheaper flights. A Google Sheet holds the routes and user emails, SerpAPI gives the prices, Telegram sends me alerts and Gmail emails everyone on the list.
- [Day 32, Birthday Wisher](Day-32/birthday-wisher): sends birthday emails and runs every day on GitHub Actions. The private birthday list is stored as a secret, so it isn't in the repo.
- [Day 38, Workout Tracker](Day-38/workout-tracker): turns a sentence like "ran 3 miles" into rows in a Google Sheet.
- [Day 46, Musical Time Machine](Day-46/musical-time-machine): scrapes the Billboard top 100 for a date you type in and automatically builds a Spotify playlist for you.

## All projects

| Day | Project | What it does | Built with |
|---|---|---|---|
| 7 | [Hangman](Day-07/hangman) | Guess the word letter by letter before your lives run out. | plain Python |
| 8 | [Caesar Cipher](Day-08/caesar-cipher) | Hide and reveal messages by shifting the letters. | plain Python |
| 9 | [Blind Auction](Day-09/blind-auction) | Collects bids and shows who bid the most. | plain Python |
| 10 | [Calculator](Day-10/calculator) | A calculator that can keep using the last answer. | plain Python |
| 11 | [Blackjack](Day-11/blackjack) | Blackjack against the computer. | plain Python |
| 12 | [Number Guessing Game](Day-12/number-guessing-game) | Guess a number from 1 to 100 in a limited number of tries. | plain Python |
| 14 | [Higher or Lower](Day-14/higher-or-lower) | Guess which of two famous accounts has more followers. | plain Python |
| 15 | [Coffee Machine](Day-15/coffee-machine) | Takes orders, checks ingredients and takes coins. | plain Python |
| 16 | [Coffee Machine (OOP)](Day-16/oop-coffee-machine) | The same machine, built with classes. | plain Python |
| 17 | [Quiz Game](Day-17/quiz-game) | A true/false quiz built with classes. | plain Python |
| 18 | [Hirst Painting](Day-18/hirst-painting) | Draws a grid of coloured dots. | turtle |
| 19 | [Etch A Sketch](Day-19/etch-a-sketch) | Draw with the keyboard. | turtle |
| 20-21 | [Snake](Day-20/snake-game) | The Snake game with a saved high score. | turtle |
| 22 | [Pong](Day-22/pong-game) | Two player Pong that gets faster. | turtle |
| 23 | [Turtle Crossing](Day-23/turtle-crossing) | Cross the road without touching a car. | turtle |
| 25 | [U.S. States Game](Day-25/us-states-game) | Name the states on a map. | turtle, pandas |
| 28 | [Pomodoro Timer](Day-28/pomodoro) | A work and break timer (alerts work on Mac only). | tkinter |
| 29 | [Password Manager](Day-29/password-manager) | Makes passwords and saves them in a file (not encrypted). | tkinter, json, pyperclip |
| 31 | [Flash Cards](Day-31/flash-card-project) | German to English flash cards that remember what you know. | tkinter, pandas |
| 32 | [Birthday Wisher](Day-32/birthday-wisher) | Sends birthday emails. Runs every day on GitHub Actions. | smtplib, pandas, GitHub Actions |
| 33 | [ISS Overhead Notifier](Day-33/iss-overhead-notifier) | Emails me when the space station is above me at night. | requests, smtplib |
| 34 | [Quizzler](Day-34/quizzler-app-api) | A true/false quiz app with questions from the internet. | tkinter, requests |
| 35 | [Rain Alert](Day-35/rain-alert) | Telegram message if rain is coming in the next 12 hours. | requests, Telegram |
| 36 | [Stock News Alert](Day-36/stock-news) | Sends news when a stock moves 5% in a day. Runs on weekdays. | requests, Telegram, GitHub Actions |
| 37 | [Habit Tracker](Day-37/habit-tracker) | Saves daily habits to a Pixela graph. | requests |
| 38 | [Workout Tracker](Day-38/workout-tracker) | Type your workout and it is saved in a Google Sheet. | requests |
| 39 | [Flight Deal Finder](Day-39/flight-deals) | Finds cheaper flights for routes in a sheet and tells me. | requests, requests-cache, Telegram, GitHub Actions |
| 40 | [Flight Deal Finder & Flight Club](Day-40/flight-club) | Finds cheaper flights and emails users in a sheet. | requests, requests-cache, Telegram, smtplib |
| 45 | [Top 100 Movies Scraper](Day-45/scrape_movie) | Scrapes Empire's top 100 movies list and saves it to a file. | requests, requests-cache, beautifulsoup4 |
| 46 | [Musical Time Machine](Day-46/musical-time-machine) | Creates a Spotify playlist of the top 100 songs from a specific date. | beautifulsoup4, spotipy |


## How to run a project

```text
git clone https://github.com/yashcontractor04/100-days-of-python.git
cd 100-days-of-python
pip install -r requirements.txt
```

Then open a project folder in the terminal and run `python main.py`. Run it from inside that folder, because some projects need files (like pictures or CSV files) that sit next to `main.py`.

- You need Python 3.12 or newer.
- Projects that use a web service need keys in a file called `.env` inside the project folder. The README of each project lists the names. `.env` is in `.gitignore`, so keys are never uploaded.
- The early terminal projects (days 7 to 16) expect you to type what the question asks for. A typing mistake (like a drink that isn't on the menu) or dividing by zero will crash them.
