from data import MENU 
order = input("What would you like? (espresso/latte/cappuccino) :") 


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_espresso():
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    if  espresso_water == resources["water"] or  espresso_water >= resources["water"]:
        if espresso_coffee == resources["coffee"] or espresso_coffee >= resources["coffee"]:
            resources["water"] -= espresso_coffee
            resources["coffee"] -= espresso_coffee
            print(" Enjoy!")

def check_latte():
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    if  latte_water == resources["water"] or  latte_water >= resources["water"]:
        if  latte_coffee == resources["water"] or latte_coffee >= resources["water"]:
            if latte_milk == resources["water"] or latte_milk >= resources["water"]:
                return True
def check_cappuccino():
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    if  cappuccino_water == resources["water"] or  cappuccino_water >= resources["water"]:
        if  cappuccino_coffee == resources["coffee"] or cappuccino_coffee >= resources["coffee"]:
            if cappuccino_milk == resources["milk"] or cappuccino_milk >= resources["milk"]:
                return True

def check_coins(cent,quarter, nickle, dollar):
  profit = 0
  espresso_cost = MENU["espresso"]["cost"]
  latte_cost = MENU["latte"]["cost"] 
  cappuccino_cost = MENU["cappuccino"]["cost"] 
  total =  espresso_cost+latte_cost+cappuccino_cost
  total_receive = cent+quarter+nickle+dollar            
  if total_receive == total:
       profit += total_receive
       return print("equal")
  elif total_receive >= total:
      owe_amount = total_receive - total
      profit += total
      return f"{owe_amount} return money"
  elif total_receive <= total:
      print('You don\'t have enough money. Here\'s is your refund.')

if order == "report":
    for resource in resources["water"]:
        print(f"{resource }: {resources[resource]}")
    
elif order == 'espresso':
    cent = float(input("Enter some cents: "))
    quarter = float(input("Enter some Quarters : "))
    nickle = float(input("Enter a nickel: "))
    dollar = float(input("Enter a dollar: "))
    
    if check_coins(cent,quarter,nickle,dollar):
        check_espresso()
    # if check_espresso(): 
    #     check_coins(cent,quarter,nickle,dollar)
    #     print("Enjoy!")
elif order == 'latte':
    cent = float(input("Enter some cents: "))
    quarter = float(input("Enter some Quarters : "))
    nickle = float(input("Enter a nickel: "))
    dollar = float(input("Enter a dollar: "))
    print()
elif order == 'cappuccino':
    cent = float(input("Enter some cents: "))
    quarter = float(input("Enter some Quarters : "))
    nickle = float(input("Enter a nickel: "))
    dollar = float(input("Enter a dollar: "))
    print()


