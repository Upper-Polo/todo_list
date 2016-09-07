# Upper-Polo To Do List App

import os

# An Item object for each user entry to their todo list.

class ToDoList:
    def __init__(self):
        self.todo_items = []

    # User adds a todo item to their list.
    def add(self, user_text):
        self.todo_items.append(user_text)
        

    # User removes a todo item to their list.
    def item_remove(self):

        # Prompt for list item #
        to_remove = input("Which Item #?")

        # Check for digit.
        if not to_remove.isdigit():
            print('invalid list option')

        # Get the value at the line item number.
        else:
            to_remove = int(to_remove)

            the_item = self.todo_items[to_remove - 1]

            self.todo_items.remove(the_item)
            

    def print_all_items(self):
        os.system("clear")
        print('To Do')

        i = 0
        while i < len(self.todo_items):
            print('{} {}'.format(i + 1, self.todo_items[i]))
            i = i + 1





