"""
Services module.

This module provides functions to manage an inventory system.
It allows adding, displaying, searching, updating, and deleting
products, as well as calculating inventory statistics.

Each product contains a name, price, and quantity.
"""
import os


def clear_screen():
    """
    Clears the terminal screen depending on the operating system.

    Uses 'cls' for Windows and 'clear' for Unix-based systems.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def add_product(inventory, name, price, quantity):
    """
    Adds a new product to the inventory.

    Args:
        inventory (list): List containing all products.
        name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity of the product.

    Returns:
        None
    """
    # Create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add product to inventory
    inventory.append(product)

    print("\nProduct added successfully")
    input("\nPress enter to return to menu")
    clear_screen()


def show_inventory(inventory):
    """
    Displays all products stored in the inventory.

    Args:
        inventory (list): List of product dictionaries.

    Returns:
        None
    """
    if not inventory:
        # Handle empty inventory case
        print("Inventory is empty")
        input("\nPress enter to return to menu")
        clear_screen()
    else:
        print("\n--- INVENTORY ---\n")

        # Iterate through all registered products
        for producto_registrado in inventory:
            print(
                "\nProduct:", producto_registrado["name"],
                "| Price:", producto_registrado["price"],
                "| Quantity:", producto_registrado["quantity"], "\n"
            )

        input("\nPress enter to return to menu")
        clear_screen()


def search_product(inventory, name):
    """
    Searches for a product by name.

    Args:
        inventory (list): List of product dictionaries.
        name (str): Name of the product to search.

    Returns:
        dict | None: The found product if it exists, otherwise None.
    """
    # Iterate through inventory to find matching product
    for product in inventory:
        if product["name"].lower() == name.lower():
            print(f"\nProduct found: {product}")
            input("\nPress enter to return to menu")
            clear_screen()
            return product

    # If no product is found
    clear_screen()
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Updates the price and/or quantity of an existing product.

    Args:
        inventory (list): List of product dictionaries.
        name (str): Name of the product to update.
        new_price (float, optional): New price value.
        new_quantity (int, optional): New quantity value.

    Returns:
        None
    """
    # Search for the product
    product = search_product(inventory, name)

    if product is None:
        print("\n", "=" * 30, "Update product", "=" * 30, "\n")
        print("Product not found")
        input("\nPress enter to return to menu")
        clear_screen()
        return

    # Update values only if provided
    if new_price is not None:
        product["price"] = new_price

    if new_quantity is not None:
        product["quantity"] = new_quantity

    print("\n", "=" * 30, "Update product", "=" * 30, "\n")
    print("Product updated")
    input("\nPress enter to return to menu")
    clear_screen()


def delete_product(inventory, name):
    """
    Removes a product from the inventory.

    Args:
        inventory (list): List of product dictionaries.
        name (str): Name of the product to remove.

    Returns:
        None
    """
    # Iterate with index to safely remove items
    for i, product in enumerate(inventory):
        if product["name"].lower() == name.lower():
            inventory.pop(i)
            print("\nProduct removed")
            input("\nPress enter to return to menu")
            clear_screen()
            return

    # If product is not found
    print("Product not found")
    input("\nPress enter to return to menu")
    clear_screen()


def calculate_stats(inventory):
    """
    Calculates and displays inventory statistics.

    Args:
        inventory (list[dict]): List of products.
            Each product must contain:
            - "name" (str)
            - "price" (float)
            - "quantity" (int)

    Returns:
        dict | None: Dictionary with calculated metrics if inventory
        is not empty, otherwise None.
    """
    clear_screen()
    print("\n", "=" * 30, "INVENTORY STATISTICS", "=" * 30, "\n")

    # Handle empty inventory
    if not inventory:
        print("No products available to calculate statistics.\n")
        input("\nPress enter to return to menu")
        clear_screen()
        return None

    # Calculate totals
    total_units = sum(product["quantity"] for product in inventory)
    total_value = sum(p["price"] * p["quantity"] for p in inventory)

    # Find most expensive product and highest stock product
    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])

    # Store results in a dictionary
    stats = {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": {
            "name": most_expensive["name"],
            "price": most_expensive["price"],
        },
        "highest_stock": {
            "name": highest_stock["name"],
            "quantity": highest_stock["quantity"],
        },
    }

    # Display results
    clear_screen()
    print("\n", "=" * 30, "INVENTORY STATISTICS", "=" * 30, "\n")
    print(f"Registered products: {len(inventory)}")
    print(f"Total units: {total_units}")
    print(f"Total inventory value: ${total_value:,.2f}")
    print(
        f"Most expensive product: {most_expensive['name']} "
        f"(${most_expensive['price']:,.2f})"
    )
    print(
        f"Highest stock product: {highest_stock['name']} "
        f"({highest_stock['quantity']} units)\n"
    )

    input("\nPress enter to return to menu")
    clear_screen()

    return stats
