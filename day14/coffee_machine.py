import subprocess

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def get_drink_name(options):
    while True:
        try:
            choice = int(input("\nWhat would you like to order: "))
            if choice in options:
                return options[choice]
            print("⚠️ Invalid choice. Select from the above list")
        except ValueError:
            print("⚠️ Enter a number")


subprocess.run(["clear"])
print("*** MENU ***")
#! SOMETHING NEW
drink_options = {}
for count, drink in enumerate(MENU, start=1):
    drink_options[count] = drink
    print(f"[{count}] {drink.capitalize()}")
drink = get_drink_name(drink_options)
