
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        quantity = validate_quantity(quantity)

        for _ in range(quantity):
            self.items.append(item)

        print(item, "added to order.")

    def calculate_total(self, menu):
        total = 0
        for item in self.items:
            price = menu.get_price(item)
            if price is not None:
                total += price
        return total

    def display_order(self, menu):
        print("\n--- YOUR ORDER ---")

        if not self.items:
            print("Your order is empty.")
            return

        quantities = {}
        for item in self.items:
            quantities[item] = quantities.get(item, 0) + 1

        for item, quantity in quantities.items():
            price = menu.get_price(item)
            print(f"{item} x {quantity} - {price * quantity} RWF")

        print("Total:", self.calculate_total(menu), "RWF")

    def apply_order_discount(self, menu, discount_percentage):
        discount_percentage = validate_discount(discount_percentage)
        total = self.calculate_total(menu)
        return apply_discount(total, discount_percentage)


def calculate_order_total(order):
    total = 0
    for item in order:
        quantity = validate_quantity(item["quantity"])
        price = validate_price(item["price"])
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


def apply_discount(total, discount_percentage):
    discount_percentage = validate_discount(discount_percentage)
    return total - total * (discount_percentage / 100)
