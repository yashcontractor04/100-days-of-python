# Day 37: Habit Tracker

Saves your daily habits to [Pixela](https://pixe.la), a website that draws a graph of your habits (a bit like the green squares on GitHub). The program talks to Pixela over the internet. There is one function for each kind of request:

- `create_user()` and `create_graph()`: set up your account and your graph. You only need these once, and `main` doesn't call them.
- `post_pixel()`: adds an entry for a date (a POST request)
- `update_pixel()`: changes the entry for a date (a PUT request)
- `delete_pixel()`: removes the entry for a date (a DELETE request)

Your token is sent with every request so Pixela knows it is you.

As it is, `python main.py` adds 2.5 hours for today to a graph called `graph1` ("Study Graph", measured in hours) and prints the link to the graph. To try the update and delete functions, remove the `#` from the lines at the bottom of the file.

## Setup

Create a file called `.env` in this folder:

```text
PIXELA_USERNAME=your_pixela_username
PIXELA_TOKEN=your_pixela_token
```

The very first time, you also need to run `create_user()` and `create_graph()` once. For example, add them under `if __name__ == "__main__":`, run the file and then remove them again.
