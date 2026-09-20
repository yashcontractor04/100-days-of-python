# ISS Overhead Nighttime Notifier
A background monitoring service that consumes the Open-Notify and Sunrise-Sunset REST APIs to calculate whether the International Space Station (ISS) is currently flying within viewing range of Berlin (+/- 5 degrees) during hours of darkness. Dispatches automated email alerts via `smtplib` over TLS.

### Tech / Concepts
* REST API consumption with query parameters using `requests`
* ISO 8601 timestamp parsing and UTC temporal alignment using `datetime.timezone.utc`
* Coordinate proximity threshold calculations (`abs(diff) <= 5`)
* TLS email dispatch with `smtplib` using shared credentials (`MY_EMAIL`, `MY_EMAIL_PASSWORD`)

### Quickstart
1. Ensure the root `requirements.txt` dependencies are installed:
   `pip install -r requirements.txt`
2. Create or verify your local `.env`:
   ```text
   MY_EMAIL=your_email@gmail.com
   MY_EMAIL_PASSWORD=your_google_app_password
3. Run the service:
   `python main.py`
