from menu import Menu
from order import Order


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.order = Order()

    def show_menu(self):
        print("\nWelcome to", self.name)
        self.menu.display_menu()

    def place_order(self, item):
        if self.menu.get_price(item) is not None:
            self.order.add_item(item)
        else:
            print("Sorry, that item is not available.")
