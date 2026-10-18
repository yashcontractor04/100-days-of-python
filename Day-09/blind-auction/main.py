from art import *

print(logo)

flag = True
bidders = {}
while flag:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bidders[name] = bid
    # TODO-3: Whether if new bids need to be added
    if input("Are there any other bidders? Type 'yes or 'no'.\n") == "no":
        flag = False

# TODO-4: Compare bids in dictionary
# winner = ""
# for name in bidders:
#     if bidders[name] > max_bid:
#         max_bid = bidders[name]
#         winner = name
winner = max(bidders, key=bidders.get)
max_bid = bidders[winner]

print("\n" * 50)

print(f"The winner is {winner} with a bid of ${max_bid}")

