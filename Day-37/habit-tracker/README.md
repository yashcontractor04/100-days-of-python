# Habit Tracker with Pixela API
A console-based habit logging client built using Python's `requests` and the Pixela REST API. Demonstrates full HTTP lifecycle semantics (`POST`, `PUT`, `DELETE`) with custom HTTP header authentication (`X-USER-TOKEN`) to maintain an active activity graph.

### Tech / Concepts
* REST HTTP request methods: `POST` (resource creation), `PUT` (state mutation), `DELETE` (removal)
* Custom token authentication in headers via `X-USER-TOKEN`
* Date formatting to ISO string tokens (`strftime('%Y%m%d')`)
* Separation of API actions into isolated operational handlers

### Quickstart
1. Install dependencies:
   `pip install -r requirements.txt`
2. Populate `.env`:
   ```text
   PIXELA_USERNAME=your_pixela_username
   PIXELA_TOKEN=your_pixela_token
3. Run the script
   `python main.py`
