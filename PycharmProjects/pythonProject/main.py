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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def hand_Money(MENU,choice):

    print("Please insert coins.")
    quarters = input("how many quarters?:")
    dimes = input("how many dimes?:")
    nickles = input("how many nickles?:")
    pennies = input("how many pennies?:")


choice = input("What would you like? (espresso/latte/cappuccino):")
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money=0.0
if choice == "report":
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}gm\nMoney:${money}")
elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
    hand_Money(MENU,choice)

