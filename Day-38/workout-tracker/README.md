# Natural Language Workout Tracker
An automated workout logging application built with Python, Nutritionix Natural Language Processing API, and Sheety API. Converts plain text exercise inputs (e.g., "ran 3 miles and walked 20 mins") into structured calorie/duration metrics and appends them directly to a Google Sheet via RESTful Bearer Token authentication.

### Tech / Concepts
* Natural language exercise processing with `Nutritionix API`
* Automated Google Sheets row creation via `Sheety API`
* Bearer Token Authorization header management (`Authorization: Bearer <TOKEN>`)
* Datetime string formatting (`strftime`)
* Environment variable injection via `python-dotenv`

### Quickstart
1. Install dependencies from the repository root:
   `pip install -r requirements.txt`
2. Create `.env` inside `Day-38/workout-tracker/`:
   ```text
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   BEARER_TOKEN=your_sheety_bearer_token
3. Run the script:
   `python main.py`
