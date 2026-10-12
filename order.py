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


def apply_discount(total, discount_percentage):
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    discount_amount = total * (discount_percentage / 100)
    final_total = total - discount_amount

    return final_total


subtotal = 16000
discount = 10

final_total = apply_discount(subtotal, discount)

print("Subtotal:", subtotal, "RWF")
print("Discount:", discount, "%")
print("Final total:", final_total, "RWF")
