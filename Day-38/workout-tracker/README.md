# Day 38: Workout Tracker

You type what you did in normal English, like "ran 3 miles and walked 20 minutes". The program sends that sentence to an exercise website (the one the course provides), which works out the duration and calories burned for each exercise. Then the program adds one row per exercise to a Google Sheet, with the date, time, exercise, duration and calories.

To write to the Google Sheet it uses Sheety, a service that lets Python read and write a Google Sheet.

## Setup

- Make a Google Sheet with a sheet called `workouts` and the columns `date`, `time`, `exercise`, `duration` and `calories`. Connect it to Sheety and turn on the "Bearer token" login.
- `SHEETY_URL` in `main.py` points to my own sheet. Replace it with the link to yours.
- `GENDER`, `WEIGHT_KG`, `HEIGHT_CM` and `AGE` at the top of `main.py` are used to work out the calories. Put in your own numbers.
- Create a file called `.env` in this folder:

  ```text
  APP_ID=your_exercise_api_app_id
  API_KEY=your_exercise_api_key
  BEARER_TOKEN=your_sheety_bearer_token
  ```

To run it: `python main.py`
