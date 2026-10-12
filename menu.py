
class Menu:
    def __init__(self):
        self.items = {
            "Burger": 3000,
            "Pizza": 5000,
            "Fries": 1500,
            "Soda": 1000
        }

    def display_menu(self):
        print("\n--- RESTAURANT MENU ---")
        for item, price in self.items.items():
            print(f"{item}: {price} RWF")

    def get_price(self, item):
        return self.items.get(item)

    def search_food(self, search_term):
        results = []
        for item, price in self.items.items():
            if search_term.lower() in item.lower():
                results.append((item, price))
        return results

    def add_menu_item(self, name, price):
        if not name.strip():
            raise ValueError("Food name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if name in self.items:
            raise ValueError("This menu item already exists.")

        self.items[name] = price
        return True

    def remove_menu_item(self, name):
        if name in self.items:
            del self.items[name]
            return True
        return False

    def update_menu_price(self, name, new_price):
        if new_price <= 0:
            raise ValueError("Price must be greater than zero.")
        if name not in self.items:
            return False

        self.items[name] = new_price
        return True
