from restaurant import Restaurant


def main():
    restaurant = Restaurant("Kigali Restaurant")

    while True:
        print("\n===== RESTAURANT SYSTEM =====")
        print("1. Display menu")
        print("2. Place order")
        print("3. View bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            restaurant.show_menu()

        elif choice == "2":
            item = input("Enter food item: ").strip().title()
            restaurant.place_order(item)

        elif choice == "3":
            restaurant.order.display_order(restaurant.menu)

        elif choice == "4":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
