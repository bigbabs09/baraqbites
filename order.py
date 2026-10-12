class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(item, "added to order.")

    def calculate_total(self, menu):
        total = 0

        for item in self.items:
            total += menu.get_price(item)

        return total

    def display_order(self, menu):
        print("\n--- YOUR ORDER ---")

        if not self.items:
            print("Your order is empty.")
            return

        for item in self.items:
            print(item, "-", menu.get_price(item), "RWF")

        print("Total:", self.calculate_total(menu), "RWF")


def calculate_order_total(order):
    total = 0

    for item in order:
        price = item["price"]
        quantity = item["quantity"]

        total += price * quantity

    return total


sample_order = [
    {"name": "Burger", "price": 5000, "quantity": 2},
    {"name": "Juice", "price": 2000, "quantity": 3}
]

total = calculate_order_total(sample_order)

print("Order total:", total, "RWF")
