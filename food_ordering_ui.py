#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Nainika's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Q':
      break
    elif user_menu_choice in 'X':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      
    elif user_menu_choice in 'N':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))

def close_order(menu_choice):
   print("\nYour Order:")
   total = 0
   
   for item in menu_choice:
     item_name, item_price, quantity = item
     extended_price = item_price * quantity
     print(f"{quantity} x {item_name}: ${extended_price}")
     total += extended_price

     tax = total * 0.07
     grand_tot = total + tax

     print(f"\nTotal: ${total:.2f}")
     print(f"Tax (7%): ${tax:.2f}")
     print(f"Grand Total: ${grand_total:.2f}")
     print("Thank you for dining with us!\n")
  
  #print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


