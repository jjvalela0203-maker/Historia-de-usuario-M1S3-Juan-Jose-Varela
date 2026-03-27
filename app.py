"""
Main module of the inventory management system.

This module controls the program execution flow through
an interactive menu. It allows the user to add products,
display the inventory, search, update, delete items, and
calculate statistics using functions from other modules.

The program runs continuously until the user selects
the exit option.
"""

from services import (
    add_product,
    show_inventory,
    search_product,
    update_product,
    delete_product,
    calculate_stats,
    clear_screen
)

from archives import (save_csv, read_csv)

inventory = []


def show_menu():
    """
    Displays the main menu of the inventory system.

    This function prints the ASCII logo and the list of
    available options for the user to interact with the system.
    """
    logo = r"""
    ██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    ██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝     ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝      ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║       ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
    """

    print(logo)
    print("\n", "=" * 30, "MENU", "=" * 30, "\n")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")


active = True

while active:
    show_menu()

    valid = True
    while valid:
        try:
            option = int(input("Select an option: "))
            if 1 <= option <= 9:
                valid = False
            else:
                clear_screen()
                print("\n", "=" * 30, "MENU", "=" * 30, "\n")
                print("\nError: Invalid input. Please enter a valid number.")
                input("\nPress enter to retry...")
                clear_screen()
        except ValueError:
            clear_screen()
            print("\n", "=" * 30, "MENU", "=" * 30, "\n")
            print("\nError: Invalid input. Please enter a number.")
            input("\nPress enter to retry...")
            clear_screen()

        show_menu()

    if option == 1:
        clear_screen()
        print("\n", "=" * 30, "Add a product", "=" * 30, "\n")

        name = input("Name: ")

        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
        except ValueError:
            print("\nInvalid price or quantity")
            input("\nPress enter to return to menu")
            clear_screen()
            continue

        if price < 0 or quantity < 0:
            print("\nNegative values are not allowed")
            continue

        add_product(inventory, name, price, quantity)

    elif option == 2:
        clear_screen()
        print("\n", "=" * 30, "INVENTORY", "=" * 30, "\n")
        show_inventory(inventory)

    elif option == 3:
        clear_screen()
        print("\n", "=" * 30, "Search product", "=" * 30, "\n")

        name = input("Enter product name: ")
        product = search_product(inventory, name)

        if not product:
            print("\n", "=" * 30, "Search product", "=" * 30, "\n")
            print("Product not found")
            input("Press enter to return to menu")
            clear_screen()

    elif option == 4:
        clear_screen()
        print("\n", "=" * 30, "Update product", "=" * 30, "\n")

        name = input("Product name to update: ")

        try:
            price = input("New price (Enter to skip): ")
            quantity = input("New quantity (Enter to skip): ")

            new_price = float(price) if price else None
            new_quantity = int(quantity) if quantity else None

        except ValueError:
            print("\nInvalid data")
            input("\nPress enter to return to menu")
            clear_screen()
            continue

        update_product(inventory, name, new_price, new_quantity)

    elif option == 5:
        clear_screen()
        print("\n", "=" * 30, "Delete product", "=" * 30, "\n")

        name = input("Product name to delete: ")
        delete_product(inventory, name)

    elif option == 6:
        calculate_stats(inventory)

    elif option == 7:
        clear_screen()
        print("\n", "=" * 30, "Save CSV", "=" * 30, "\n")

        path = input("Enter file name (e.g., inventory.csv): ")
        if not path.endswith(".csv"):
            path += ".csv"

        save_csv(inventory, path)

    elif option == 8:
        clear_screen()
        print("\n", "=" * 30, "LOAD CSV", "=" * 30, "\n")

        path = input("Enter CSV file path: ")
        new_products, errors = read_csv(path)

        if not new_products:
            clear_screen()
            print("\n", "=" * 30, "LOAD CSV", "=" * 30, "\n")
            print("No products loaded")
            input("\nPress enter to return to menu")
            clear_screen()
            continue

        decision = input("Overwrite current inventory? (Y/N): ").lower()

        if decision == "y":
            inventory.clear()
            inventory.extend(new_products)
            print("Inventory replaced")
            input("\nPress enter to return to menu")
            clear_screen()

        else:
            for new in new_products:
                existing = search_product(inventory, new["name"])

                if existing:
                    existing["quantity"] += new["quantity"]
                    existing["price"] = new["price"]
                else:
                    inventory.append(new)

            print("\n", "=" * 30, "LOAD CSV", "=" * 30, "\n")
            print("Inventory merged")

        print(f"\nProducts loaded: {len(new_products)}")
        print(f"\nInvalid rows: {errors}")
        input("\nPress enter to return to menu")
        clear_screen()

    elif option == 9:
        clear_screen()
        print("\n", "=" * 30, "Exit", "=" * 30, "\n")
        print("Exiting program...")
        active = False
