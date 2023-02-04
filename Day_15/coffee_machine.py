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


def check_inventory(your_decision=''):
    user_choice = MENU[your_decision]
    if resources['water'] < user_choice['ingredients']['water']:
      return 'water'
    if resources['milk'] < user_choice['ingredients']['milk']:
      return 'milk'
    if resources['coffee'] < user_choice['ingredients']['coffee']:
      return 'coffee'
    return ''


def update_resource(your_decision=''):
    user_choice = MENU[your_decision]
    resources['water'] = resources['water'] - user_choice['ingredients']['water']
    resources['milk'] = resources['milk'] - user_choice['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - \
        user_choice['ingredients']['coffee']
    resources['wallet'] = user_choice['cost']


def check_price(quaters=0, dimes=0, nickles=0, pennies=0, your_decision=''):
    user_choice_amount = MENU[your_decision]['cost']
    total_amount = 0
    total_amount = (quaters*25) + total_amount
    total_amount = (dimes*10) + total_amount
    total_amount = (nickles*5) + total_amount
    total_amount = (pennies*1) + total_amount
    #print("\n total_amount",total_amount)
    total_amount = total_amount/100
    #print("\n total_amount",total_amount)
    if user_choice_amount > total_amount:
        print("You have got less money")
        return False
    elif user_choice_amount < total_amount:
        left_money = total_amount - user_choice_amount
        print(f"your cahnges {round(left_money,2)} please collect.")
        return True
    return True


def cofee_machine():
  while True:
    your_decision = input("What would you like? (espresso/latte/cappuccino)")
    if your_decision == 'report':
        print(resources)
    else:
        inventory = check_inventory(your_decision=your_decision)
        if inventory != '':
            print(f"The {inventory} is not suffiecient for {your_decision}")
            return
        print("Please insert Coins")
        quaters = int(input("How many quaters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        price_check = check_price(quaters=quaters, dimes=dimes,
                                  nickles=nickles, pennies=pennies, your_decision=your_decision)
        if price_check == False:
            return
        print("here is your latte Enjoy!")
        update_resource(your_decision=your_decision)


cofee_machine()
