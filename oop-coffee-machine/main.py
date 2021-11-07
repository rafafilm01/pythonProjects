from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_mkr = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
powered_on = True



while powered_on:
    options = menu.get_items()
    choice = input(f'What would you like ? {options} : ')
    if choice =='OFF':
        powered_on = False
        print('powering down...')
    elif choice == 'report':
        coffee_mkr.report()
        money_machine.report()
    else:
        drink =menu.find_drink(choice)
        if coffee_mkr.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost) :
                coffee_mkr.make_coffee(drink)