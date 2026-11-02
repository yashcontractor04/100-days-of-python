# Day 49: Gym Booking Bot

Automates booking gym classes using Selenium. It logs into the portal, filters the schedule for Tuesday and Thursday classes at 6:00 PM, books open spots or joins waitlists, and cross-checks the bookings on the My Bookings page.

Includes custom retry logic to handle simulated network drops and page timeouts during login and booking steps.

## Setup

Create a file called `.env` in this folder:

```text
GYM_EMAIL=your_email@test.com
GYM_PASSWORD=your_password
```
To run it: `python main.py`