from data import MENU 
order = input("What would you like? (espresso/latte/cappuccino) :") 
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_espresso(water, coffee, cost):
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    espresso_cost = MENU["espresso"]["ingredients"]["cost"]
    if  espresso_water == water or  espresso_water >= water:
        if espresso_coffee == coffee or espresso_coffee >= coffee:
            if espresso_coffee == cost or espresso_cost >= cost:
                print("here's your coffe, Enjoy!")

def check_latte(water, milk, coffee, cost):
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_cost = MENU["latte"]["ingredients"]["cost"]
    if  latte_water == water or  latte_water >= water:
        if  latte_coffee == coffee or latte_coffee >= coffee:
            if latte_milk == milk or latte_milk >= milk:
                if latte_coffee == cost or latte_cost >= cost:
                    print("here's your coffe, Enjoy!")
                    
def check_cappuccino(water, milk, coffee, cost):
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_cost = MENU["cappuccino"]["ingredients"]["cost"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    if  cappuccino_water == water or  cappuccino_water >= water:
        if  cappuccino_coffee == coffee or cappuccino_coffee >= coffee:
            if cappuccino_milk == milk or cappuccino_milk >= milk:
                if cappuccino_coffee == cost or cappuccino_cost >= cost:
                    print("here's your coffe, Enjoy!")

if order == "report":
    for resource in resources:
        print(f"{resource }: {resources[resource]}")
    print(f"Money: {profit}")
elif order == 'espresso':
    print()
elif order == 'latte':
    print()
elif order == 'cappuccino':
    print()
