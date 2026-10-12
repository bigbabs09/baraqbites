
from menu import Menu
from order import Order


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.order = Order()
        self.is_open = True

    def show_menu(self):
        print("\nWelcome to", self.name)
        self.menu.display_menu()

    def place_order(self, item, quantity=1):
        if not self.is_open:
            print("Sorry, the restaurant is closed.")
            return

        if self.menu.get_price(item) is not None:
            self.order.add_item(item, quantity)
        else:
            print("Sorry, that item is not available.")

    def add_menu_item(self, name, price):
        return self.menu.add_menu_item(name, price)

    def remove_menu_item(self, name):
        return self.menu.remove_menu_item(name)

    def update_menu_price(self, name, new_price):
        return self.menu.update_menu_price(name, new_price)

    def restaurant_status(self):
        if self.is_open:
            return "Restaurant is open."
        return "Restaurant is closed."
