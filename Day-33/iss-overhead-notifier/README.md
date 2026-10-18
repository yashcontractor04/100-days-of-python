# Day 33: ISS Overhead Notifier

The ISS (International Space Station) flies around the Earth. This program emails you when it is above you at night, so you can go outside and see it.

Every 60 seconds it checks two things:

1. Is the ISS close to my location (within 5 degrees in each direction)? The position comes from the Open Notify website.
2. Is it dark outside right now? The sunrise and sunset times come from sunrise-sunset.org.

If both are true, it sends you an email. My location is set at the top of `main.py` (`MY_LAT` and `MY_LONG`) and is currently Berlin. Neither website needs a key.

## Setup

Create a file called `.env` in this folder:

```text
MY_EMAIL=you@gmail.com
MY_EMAIL_PASSWORD=your_gmail_app_password
```

Use a Gmail "app password" (a special password just for apps), not your normal one.

To run it: `python main.py`. It keeps running until you press Ctrl+C. If there is a network problem, it prints the error and tries again.
