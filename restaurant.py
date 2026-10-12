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

    def add_menu_item(menu, name, category, price):
        if not name.strip():
            raise ValueError("Food name cannot be empty.")

        if not category.strip():
            raise ValueError("Category cannot be empty.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        for item in menu:
            if item["name"].lower() == name.lower():
                raise ValueError("This menu item already exists.")

        new_item = {
            "name": name,
            "category": category,
            "price": price
        }

        menu.append(new_item)
        return new_item

    def remove_menu_item(menu, name):
        for item in menu:
            if item["name"].lower() == name.lower():
                menu.remove(item)
                return True

        return False

    def update_menu_price(menu, name, new_price):
        if new_price <= 0:
            raise ValueError("Price must be greater than zero.")

        for item in menu:
            if item["name"].lower() == name.lower():
                item["price"] = new_price
                return True

        return False

    def restaurant_status(is_open):
        if is_open:
            return "Restaurant is open."
        return "Restaurant is closed."

