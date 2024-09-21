#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)
  return None, 0

def display_items():
  

    print("Menu:")
    for item in data.menu_items:
        item_number, item_name, item_price = item.split(' ')
        print(f"{item_number}: {item_name} - ${item_price}")


def get_item_number():
    """
    Prompts user to enter a valid item code and quantity.
    Allows user to input 'done' to finish ordering.
    """
    display_items()  # Display menu items before asking for input
    while True:
        order_item = input("Enter dish number and quantity (e.g., D1 2), or 'done' to finish: ").strip()
        if order_item.lower() == 'done':  # If 'done' (any case), return 'done'
            return 'done'
        order_parts = order_item.split()
        if len(order_parts) == 2 and order_parts[0] in data.all_items and order_parts[1].isdigit():
            return order_item  # If valid dish number and quantity, return the input
        else:
            print("Invalid input format. Please enter a valid dish number and quantity, or 'done' to finish.")
      
def display_current_order(order):
    #Displays the current items in the order.
    print("Current order:")
    
    # Debugging statement to see the structure of the current order
    print(f"Order list: {order}")
    
    for code, name, qty, price in order:
        price = int(price)  # Ensure price is an integer
        print(f"{code+name} - ${price }")