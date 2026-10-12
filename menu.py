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
