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
        else:
            print("Invalid choice, please select N, X, or Q")

def make_order(orders):
    """
    Function to make a new order.
    Adds items to the orders list.
    """
    user_selection = functions.get_item_number()
    item_code, quantity = user_selection.split()
    quantity = int(quantity)
    
    item_name, item_price = functions.get_item_information(item_code)
    
    if item_name:
        orders.append((item_name, item_price, quantity))
        print(f"Added {quantity} x {item_name} to your order.")
    else:
        print("Invalid item selected.")

def close_order(orders):
    """
    Function to close the order and print the receipt.
    Prints the list of items ordered, extended price, total, tax, and grand total.
    """
    print("\nYour Order:")
    total = 0

    for item in orders:
        item_name, item_price, quantity = item
        extended_price = item_price * quantity
        print(f"{quantity} x {item_name}: ${extended_price:.2f}")
        total += extended_price

    tax = total * 0.07  # Assuming 7% tax
    grand_total = total + tax

    print(f"\nTotal: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")


if __name__ == '__main__':
    show_main_menu()
