# 1. Define your custom exception class
class OutOfStockError(Exception):
    """Exception raised when an item is out of stock."""
    pass

# 2. Define your product inventory (global scope)
product_inventory = {
    "apple": 10,
    "orange": 0,  # Example of an item that is out of stock
    "banana": 5,
    "grapes": 20,
}

# 3. Define your purchase_item function
def purchase_item(item, quantity):
    """
    Attempts to purchase a specified quantity of an item from inventory.

    Args:
        item (str): The name of the item to purchase.
        quantity (int): The quantity to purchase.

    Raises:
        ValueError: If the item is not found, or if there's insufficient stock.
        OutOfStockError: If the item is completely out of stock (quantity is 0).
    """
    # Check if the item exists in the inventory
    if item not in product_inventory:
        raise ValueError(f"Sorry, '{item}' is not available in our inventory.")

    # Check if the item is completely out of stock
    if product_inventory[item] == 0:
        raise OutOfStockError(f"'{item}' is currently out of stock.")

    # Check if there's enough stock for the requested quantity
    if product_inventory[item] < quantity:
        raise ValueError(f"Not enough '{item}' in stock. Available: {product_inventory[item]}, Requested: {quantity}.")
    
    # If all checks pass, proceed with purchase
    product_inventory[item] -= quantity
    print(f"Successfully purchased {quantity} of '{item}'. Remaining: {product_inventory[item]} of {item}.")


# 4. Testing the Custom Exception and other scenarios
if __name__ == "__main__":
    print("--- Initial Inventory ---")
    for item, qty in product_inventory.items():
        print(f"{item}: {qty}")
    print("-" * 25)

    print("\nAttempting to purchase 3 apples...")
    try:
        purchase_item("apple", 3)  # Purchase successful
    except (OutOfStockError, ValueError) as e:
        print(f"Purchase Error for 'apple' (3): {e}")
    print("-" * 25)

    print("\nAttempting to purchase 1 orange...")
    try:
        purchase_item("orange", 1)  # Raises OutOfStockError
    except (OutOfStockError, ValueError) as e:
        print(f"Purchase Error for 'orange' (1): {e}")
    print("-" * 25)

    print("\nAttempting to purchase 1 watermelon...")
    try:
        purchase_item("watermelon", 1)  # Item not available (raises ValueError)
    except (OutOfStockError, ValueError) as e:
        print(f"Purchase Error for 'watermelon' (1): {e}")
    print("-" * 25)

    print("\nAttempting to purchase 10 bananas...")
    try:
        purchase_item("banana", 10)  # Not enough stock (raises ValueError)
    except (OutOfStockError, ValueError) as e:
        print(f"Purchase Error for 'banana' (10): {e}")
    print("-" * 25)

    print("\nAttempting to purchase 5 grapes...")
    try:
        purchase_item("grapes", 5) # Successful purchase
    except (OutOfStockError, ValueError) as e:
        print(f"Purchase Error for 'grapes' (5): {e}")
    print("-" * 25)

    print("\n--- Final Inventory ---")
    for item, qty in product_inventory.items():
        print(f"{item}: {qty}")
