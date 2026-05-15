import subprocess

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_menu():
    print("*** MENU ***")
    drink_options = {}
    for count, drink in enumerate(MENU, start=1):
        drink_options[count] = drink
        print(f"[{count}] {drink.capitalize()}")
    return drink_options


def get_drink_name(options):
    while True:
        try:
            choice = int(input("\nWhat would you like to order: "))
            if choice in options:
                return options[choice]
            print("⚠️ Invalid choice. Select from the above list")
        except ValueError:
            print("⚠️ Enter a number")


def take_money():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    return round(
        (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01), 2
    )


def enough_money(money, drink_cost):
    return money < drink_cost


def main():
    profit = 0
    subprocess.run(["clear"])
    drink_options = show_menu()
    drink = get_drink_name(drink_options)
    drink_ingredients = MENU[drink]["ingredients"]
    for resource in resources:
        if resources[resource] < drink_ingredients[resource]:
            print(f"‼️ There is not enough {resource}. Sorry for the inconvenience")
            return "Have a good day!"
    money = take_money()
    drink_cost = MENU[drink]["cost"]
    if enough_money(money, drink_cost):
        print("\n⚠️ Sorry, you didn't put in enough money. Here's your refund.")
        return "Have a good day!"
    resources[resource] -= drink_ingredients[resource]
    profit += drink_cost
    change = round(money - drink_cost, 2)
    if change > 0:
        print(f"\nYour change ₹{change}")
    print(f"And here's your {drink} ☕️. Enjoy!")


if __name__ == "__main__":
    main()
