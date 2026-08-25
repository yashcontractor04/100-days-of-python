MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 4. Check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
    return True

# TODO 5. Process coins.
def process_coins():
    print("Please insert coins.")
    total = 0.25 * int(input("how many quarters?: "))
    total += 0.10 * int(input("how many dimes?: "))
    total += 0.05 * int(input("how many nickles?: "))
    total += 0.01 * int(input("how many pennies?: "))
    return total

# TODO 6. Check if transaction is successful
def is_transaction_successful(coffee, total):
    global profit
    if total >= coffee["cost"]:
        change = round(total - coffee["cost"], 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        profit += coffee["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 7. Make Coffee.
def make_coffee(coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee} ☕️. Enjoy!”.")

is_on = True
while is_on:

    # TODO 1. Prompt user (check user intention)
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        is_on = False
    # TODO 3. Print report (show current resource values)
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient((drink["ingredients"])):
            money_put_in = process_coins()
            if is_transaction_successful(drink, money_put_in):
                make_coffee(user_input, drink["ingredients"])