"""
CSV persistence module for the inventory management system.

This module provides functionality to save and load inventory data
from CSV files. It ensures basic validation such as correct headers,
data types, and non-negative values.
"""

from services import clear_screen


def save_csv(inventory, rute, incluir_header=True):
    """
    Saves the inventory to a CSV file.

    Args:
        inventory (list[dict]): List of products with structure:
            {"name": str, "price": float, "quantity": int}
        rute (str): File path where the CSV will be saved.
        incluir_header (bool): Whether to include the header row.

    Returns:
        None
    """
    # Check if inventory is empty
    if not inventory:
        print("No products in inventory to save.\n")
        input("Press enter to return to menu")
        clear_screen()
        return

    try:
        # Open file in write mode
        with open(rute, "w", newline="", encoding="utf-8") as archive:

            # Write header if required
            if incluir_header:
                archive.write("name,price,quantity\n")

            # Write each product as a CSV row
            for product in inventory:
                line = f"{product['name']},{product['price']},{product['quantity']}\n"
                archive.write(line)

        print(f"Inventory saved to: {rute}\n")
        input("Press enter to return to menu")
        clear_screen()

    except PermissionError:
        print("Error: You do not have permission to write in this location.\n")

    except FileNotFoundError:
        print("Error: The specified path does not exist.\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")


def read_csv(rute):
    """
    Loads a CSV file and returns a list of valid products.

    Args:
        rute (str): Path to the CSV file.

    Returns:
        tuple: (list_of_products, invalid_rows_count)
    """
    charge_inventory = []
    invalid_lines = 0

    try:
        # Open file in read mode
        with open(rute, "r", encoding="utf-8") as archive:

            # Read all lines
            lines = archive.readlines()

            # Validate empty file
            if not lines:
                print("The file is empty")
                input("\nPress enter to return to menu")
                clear_screen()
                return [], 0

            # Validate header
            header = lines[0].strip()
            if header != "name,price,quantity":
                print("Invalid header")
                input("\nPress enter to return to menu")
                clear_screen()
                return [], 0

            # Process rows
            for line in lines[1:]:
                partes = line.strip().split(",")

                # Validate column count
                if len(partes) != 3:
                    invalid_lines += 1
                    continue

                name, price, quantity = partes

                try:
                    price = float(price)
                    quantity = int(quantity)

                    # Validate non-negative values
                    if price < 0 or quantity < 0:
                        invalid_lines += 1
                        continue

                    # Create product dictionary
                    product = {
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    }

                    charge_inventory.append(product)

                except ValueError:
                    # Invalid data type
                    invalid_lines += 1
                    continue

        return charge_inventory, invalid_lines

    except FileNotFoundError:
        print("Error: File not found")
        input("\nPress enter to return to menu")
        clear_screen()
        return [], 0

    except UnicodeDecodeError:
        print("Error: File encoding issue")
        input("\nPress enter to return to menu")
        clear_screen()
        return [], 0

    except Exception as e:
        print(f"Unexpected error: {e}")
        input("\nPress enter to return to menu")
        clear_screen()
        return [], 0