# Upper-Polo To Do List App

from item import Item
from item_list import ItemList

def main():
    while True:
        # Display menu
        print("1. Add Item")
        print("2. Remove Item")
        print("3. List Items")
        print("0. Exit")
        
        # Get user input
        user_in = int(input())
        
        # Add item
        if user_in == 1:
            print("Add Item")
        
        # Remove item
        elif user_in == 2:
            print("Remove Item")
        
        # Show items in item_list
        elif user_in == 3:
            print("Add Item")

        # Exit program
        elif user_in == 0:
            exit(0)

        else:
            print("invalid menu option")

main()