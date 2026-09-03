import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
tries = 0
if difficulty == "easy":
    tries = 10
else:
    tries = 5

while tries >= 0:
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        break
    print("Guess again.")
    tries -= 1

if tries == 0:
    print("You've run out of guesses.")
    print(f"The answer was {number}.")