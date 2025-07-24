# shopping_list_manager.py

def display_menu():
    """Displays the main menu to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")

        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for item in shopping_list:
                    print(f"- {item}")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
