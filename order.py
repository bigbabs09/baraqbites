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


def validate_quantity(quantity):
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a whole number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price):
    try:
        price = float(price)
    except (ValueError, TypeError):
        raise ValueError("Price must be a number.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price


def validate_discount(discount):
    try:
        discount = float(discount)
    except (ValueError, TypeError):
        raise ValueError("Discount must be a number.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    return discount


try:
    quantity = validate_quantity("abc")
    print(quantity)
except ValueError as error:
    print("Invalid input:", error)

try:
    quantity = validate_quantity(-3)
    print(quantity)
except ValueError as error:
    print("Invalid input:", error)

try:
    discount = validate_discount(120)
    print(discount)
except ValueError as error:
    print("Invalid input:", error)



sample_order = [
    {"name": "Burger", "price": 5000, "quantity": 2},
    {"name": "Juice", "price": 2000, "quantity": 3}
]

total = calculate_order_total(sample_order)

print("Order total:", total, "RWF")
