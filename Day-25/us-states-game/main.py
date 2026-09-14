import turtle
import pandas as pd

# Display & Canvas Configuration
screen = turtle.Screen()
screen.title("U.S. States Game")

# Register and set the background map graphic
IMAGE_PATH = "blank_states_img.gif"
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Load dataset and extract ground-truth state names
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop terminates when all 50 states are guessed or user exits
while len(guessed_states) < 50:
    # Prompt for input and normalize string casing
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()

    # Early exit condition: serialize missed states to CSV
    if answer_state == "Exit":
        # List comprehension to compute set difference preserving order
        states_to_learn = [states for states in all_states if states not in guessed_states]
        to_learn = pd.DataFrame(states_to_learn)
        to_learn.to_csv("states_to_learn.csv")
        break

    # Valid guess handling: verify match and avoid duplicate entries
    if answer_state in all_states:
        guessed_states.append(answer_state)

        # Instantiate dedicated text-writing turtle
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        # Filter DataFrame row for matching state coordinates
        state_data = data[data.state == answer_state]
        # .item() extracts raw scalar values from single-element pandas Series
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()