import random

from game_data import data as gd
import art

def description(person):
    name = person.get('name')
    profession = person.get('description')
    country = person.get('country')
    return f"{name}, a {profession}, from {country}"

def compare(person_a, person_b):
    return person_a.get('follower_count') > person_b.get('follower_count')


print(art.logo)

score = 0

b = random.choice(gd)

while True:

    a = b
    b = random.choice(gd)
    if a == b:
        b = random.choice(gd)

    print(f"Compare A: {description(a)}")
    print(art.vs)
    print(f"Against B: {description(b)}\n")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 100)
    print(art.logo)

    if (answer == "a" and compare(a, b)) or (answer == "b" and compare(b, a)):
        score += 1
        print(f"You're right! Current score: {score}.\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}\n")
        break



