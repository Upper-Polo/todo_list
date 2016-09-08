# Upper-Polo To Do List App


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

        print_menu()

        # Get user input
        user_in = input()
        
        # Add item
        if user_in == "1":
            print("Add Item")
            my_item = input("Please enter To-Do item\n")
            my_list.add(my_item)
            print(my_list.todo_items[-1])
        
        # Remove item
        elif user_in == "2":
            my_list.print_all_items()
            my_list.item_remove()

        
        # Show items in item_list
        elif user_in == "3":
            my_list.print_all_items()

        # Mark item complete.

        elif user_in == "4":
            my_list.print_all_items()
            my_list.item_mark_complete()

        # Exit program
        elif user_in == "0":
            exit("0")

        else:
            print("invalid menu option")

main()
