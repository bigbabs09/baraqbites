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


def search_food(menu, search_term):
    results = []

    for item in menu:
        name = item["name"].lower()
        category = item["category"].lower()

        if search_term.lower() in name or search_term.lower() in category:
            results.append(item)

    return results


menu = [
    {"name": "Beef Burger", "category": "Fast Food", "price": 5000},
    {"name": "Chicken Pizza", "category": "Fast Food", "price": 7000},
    {"name": "Orange Juice", "category": "Drinks", "price": 2000}
]

results = search_food(menu, "burger")

if results:
    for item in results:
        print(item["name"], "-", item["price"], "RWF")
else:
    print("No food found.")
