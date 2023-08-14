from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    order_name = input(f"What would you like? {menu.get_items()}:")
    if order_name == "off":
        is_machine_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             coffee_maker.make_coffee(drink)

