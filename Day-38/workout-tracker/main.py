import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Personal physical parameters for Nutritionix metabolic calculations
GENDER = 'male'
WEIGHT_KG = 87
HEIGHT_CM = 183
AGE = 22

# API Endpoints
NUTRITIONIX_URL = 'https://app.100daysofpython.dev/v1/nutrition/natural/exercise'
SHEETY_URL = 'https://api.sheety.co/54e10fae340fc530e5e332be4a63d7c8/myWorkouts/workouts'

# Environment credentials
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

def track_workout():
    """Parses natural language exercise input via Nutritionix API and logs result rows to Google Sheets via Sheety API."""
    user_input = input('Tell me which exercise you did: ')

    # Query Nutritionix API for natural language processing
    api_headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }
    data_api = {
        'query': user_input,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER,
    }

    api_response = requests.post(NUTRITIONIX_URL, json=data_api, headers=api_headers)
    api_response.raise_for_status()
    result = api_response.json()

    now = datetime.now()
    today_date = now.strftime('%d/%m/%Y')
    time_now = now.strftime('%H:%M')

    # Sheety API authentication header
    sheety_headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
        'Content-Type': 'application/json',
    }

    # Iterate over parsed exercises and append rows to Google Sheets
    for exercise in result['exercises']:
        data_workout = {
            'workout': {
                'date': today_date,
                'time': time_now,
                'exercise': exercise['name'].title(),
                'duration': exercise['duration_min'],
                'calories': exercise['nf_calories'],
            }
        }
        sheety_response = requests.post(SHEETY_URL, json=data_workout, headers=sheety_headers)
        sheety_response.raise_for_status()
        print(f"Logged: {exercise['name'].title()} -> Sheety status {sheety_response.status_code}")


if __name__ == "__main__":
    track_workout()