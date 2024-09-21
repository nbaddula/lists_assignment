# user interface to the main menu
import data
import functions

def show_main_menu():
    orders = []  
    while True:
        print("Nainika's Diner")  
        print("__________")
        print('N for a new order')
        print('X for close orders and print the check')
        print('C to change an order')
        print('Q for quit')
        user_menu_choice = input('Your choice: ').upper()
        
        if user_menu_choice == 'Q':
            break
        elif user_menu_choice == 'X':
            if orders:
                close_order(orders)
                orders = []  # Reset the orders list after closing the order
            else:
                print("No orders to close.")
        elif user_menu_choice == 'N':
            print('New order')
            make_order(orders)
        elif user_menu_choice == 'C':
            if orders:
                change_order(orders)
            else:
                print("No items to change in the order.")
        else:
            print("Invalid choice, please select N, C, X, or Q")

def make_order(orders):
    """
    Function to make a new order.
    Adds items to the orders list continuously until the user types 'done'.
    """
    print("Enter 'done' when you are finished adding items.")
    while True:
        user_selection = functions.get_item_number()
        if user_selection.lower() == 'done':  # Stop adding items when 'done' is typed
            break
        try:
            item_code, quantity = user_selection.split()
            quantity = int(quantity)
        
            item_name, item_price = functions.get_item_information(item_code)
        
            if item_name:
                orders.append((item_code, item_name, item_price, quantity))
                print(f"Added {quantity} x {item_name} to your order.")
            else:
                print("Invalid item selected.")
        except ValueError:
            print("Invalid input, enter in the format 'D1 2', or 'done' to finish.")


def close_order(orders):
    """
    Function to close the order and print the receipt.
    Prints the list of items ordered, extended price, total, tax, and grand total.
    """
    print("\nYour Order:")
    total = 0

    for item in orders:
        item_code, item_name, item_price, quantity = item
        extended_price = float(item_price) * quantity  # Convert item_price to float just to be sure it's a number
        print(f"{quantity} x {item_name}: ${extended_price:.2f}")  # Ensure formatting is for numbers
        total += extended_price

    tax = total * 0.07  # Assuming 7% tax
    grand_total = total + tax

    print(f"\nTotal: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")


def display_current_order(orders):
    """
    Displays the current items in the order.
    """
    if not orders:
        print("No items in the order.")
    else:
        for item_code, item_name, item_price, quantity in orders:
            extended_price = item_price * quantity
            print(f"{quantity} x {item_name}: ${extended_price:.2f}")

def change_order(orders):
    """
    Function to change an order.
    Allows user to either remove or update the quantity of an existing order.
    """
    print("\nCurrent order:")
    display_current_order(orders)
    while True:
        print("\nChange Options:")
        print("1. Remove an item")
        print("2. Update the quantity of an item")
        print("3. Go back to main menu")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':  # Remove an item by item code
            item_code_to_remove = input("Enter the item code you want to remove: ")
            orders[:] = [order for order in orders if order[0] != item_code_to_remove]
            print(f"{item_code_to_remove} removed from the order.")
        elif choice == '2':  # Update the quantity by item code
            item_code_to_update = input("Enter the item code you want to update the quantity for: ")
            new_quantity = int(input(f"Enter new quantity for {item_code_to_update}: "))
            for i, order in enumerate(orders):
                if order[0] == item_code_to_update:  
                    orders[i] = (order[0], order[1], order[2], new_quantity)  
                    print(f"Updated {order[1]} to {new_quantity} quantity.")
                    break
            else:
                print(f"{item_code_to_update} not found in the order.")
        elif choice == '3':  # Go back to main menu
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")



if __name__ == '__main__':
    show_main_menu()
