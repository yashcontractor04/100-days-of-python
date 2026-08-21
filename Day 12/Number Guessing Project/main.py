import random

logo = r"""  ________                                 __  .__                                  ___.                 
 /  _____/ __ __   ____   ______ ______  _/  |_|  |__   ____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  \   __\  |  \_/ __ \    /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |  | |   Y  \  ___/   |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |__| |___|  /\___  >  |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/              \/     \/        \/            \/    \/     \/       
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