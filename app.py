# app.py - Upper-Polo To Do List App

# This file defines a function named 'main' that 
# implements the app runtime loop.

from todoclass import ToDoList

def print_menu():
    # Display menu
    print("\n\n1. Add Item")
    print("2. Remove Item")
    print("3. List Items")
    print("4. Mark Done")
    print("0. Exit\n\n")


def main():
    my_list = ToDoList()
    
    while True:

        # Print todo list and menu on each iteration.
        my_list.print_todo_list()
        print_menu()

        # Get user input
        user_in = input()
        
        # Add item
        if user_in == "1":
            print("Add Item")
            my_item = input("Please enter To-Do item\n")
            my_list.add(my_item)
                    
        # Remove item
        elif user_in == "2":
            my_list.print_todo_list()
            my_list.item_remove()

        # Show items in item_list
        elif user_in == "3":
            my_list.print_todo_list()

        # Mark item complete.
        elif user_in == "4":
            my_list.print_todo_list()
            my_list.item_mark_complete()

        # Exit program
        elif user_in == "0":
            exit("0")

        else:
            print("invalid menu option")

main()
