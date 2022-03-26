from data import MENU , resources
order = input("What would you like? (espresso/latte/cappuccino) :") 
profit = 0
if order == "report":
    for resource in resources:
        print(f"{resource }: {resources[resource]}")
    print(f"Money: {profit}")