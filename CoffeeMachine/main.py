# Required Data

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

money = 0
machine_on = True
# TODO: 1. - Prompt the user by asking "What would you like? (espresso/latte/cappuccino)"


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    # TODO: 2. - Turn off the coffee machine by entering "off" to the prompt -- Done with first todo --

    if choice == "off":
        machine_on = False
        print("Goodbye")

    # TODO: 3. - Print report
    elif choice == "report":
        print(f'''
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${money}
        ''')
    else:
        # TODO: 4. - Check if resource is sufficient
        drink = MENU[choice]
        needed_ingredients = drink["ingredients"]
        print(needed_ingredients)
        if resources["water"] > needed_ingredients["water"]:
            if resources["milk"] > needed_ingredients["milk"]:
                if resources["coffee"] > needed_ingredients["coffee"]:
                    # TODO: 5. - Process coin
                    pennies = int(input("How many Pennies? ")) * 0.01
                    nickles = int(input("How many Nickles? ")) * 0.05
                    dimes = int(input("How many Dimes? ")) * 0.01
                    quarters = int(input("How many Quarters? ")) * 0.25

                    received_money = pennies + nickles + dimes + quarters

                    # TODO: 6. - Check Transaction successful
                    coffee_wanted = choice
                    cost = MENU[coffee_wanted]["cost"]
                    if cost > received_money:
                        print("Sorry, that's not enough money. Money refunded")
                    else:
                        # TODO: 7. - Make Coffee
                        print(drink["water"])
                        resources["water"] -= drink["water"]
                        resources["milk"] -= drink["milk"]
                        resources["coffee"] -= drink["coffee"]
                        balance = received_money - cost
                        money += cost
                        print(f"Here's your {choice}, Enjoy!")
                        if balance > 0:
                            print(f"Here's you ${balance} balance")
                else:
                    print("There is no enough coffee")
            else:
                print("There is no enough milk")
        else:
            print("There is no enough water")



