from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

continue_ = True
CoffeeMak = CoffeeMaker()
Menu = Menu()
#MenuItem = MenuItem()
MoneyMachine = MoneyMachine()
while continue_ == True:
  user_choice = input("What would you like? (espresso/latte/cappuccino/):")
  if user_choice == 'off':
    continue_ = False
  elif user_choice == 'report':
    CoffeeMak.report()
    MoneyMachine.report()
  else:
    user_choice = Menu.find_drink(user_choice)
    resources_available = CoffeeMak.is_resource_sufficient(user_choice)
    if resources_available:
      #MoneyMachine.process_coins()
      payment_result = MoneyMachine.make_payment(user_choice.cost)
      if payment_result:
        CoffeeMak.make_coffee(user_choice)
        
      