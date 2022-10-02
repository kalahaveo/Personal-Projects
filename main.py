MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def print_report():
    """Gives user a report of coffee machine ingredient inventory"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    """Checks if the machine has enough resources for the ordered drink and returns a boolean"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
        return True


def process_coins():
    print(f'The price is ${drink["cost"]}')
    print("Please insert coins.")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    total_input_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_input_money


def is_transaction_successful():
    """Returns True if transaction in successful, false if not"""
    if payment >= drink['cost']:
        change = round(payment - drink['cost'],2)
        print(f"Here is your change of ${change}")
        global profit
        profit += drink['cost']
        return True
    else:
        print("Sorry, that's not enough money.  Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


machine_on = True

while machine_on:
    # 1. Prompt user for drink selection
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 2. Turn off Coffee Machine by entering "off" command to the prompt
    if user_input == "off":
        print("Goodbye")
        machine_on = False
    # 3. Print report
    elif user_input == "report":
        print_report()
    # 4. Check resources sufficient?
    else:  # user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = MENU[user_input]
        enough_resources = check_resources(drink['ingredients'])
        if enough_resources:
            payment = process_coins()
            if is_transaction_successful():
                make_coffee(user_input, drink["ingredients"])
