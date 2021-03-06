# todoclass.py - Upper-Polo To Do List App

# This module defines the ToDoList class that represents
# the core storage and functionality of a todo list.

import os

# Our Item module
from item import Item

# An Item object for each user entry to their todo list.

class ToDoList:
    def __init__(self):
        self.todo_items = []

    # User adds a todo item to their list.
    def add(self, user_text):

        new_user_item = Item(user_text) 
        self.todo_items.append(new_user_item)
        
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

    # User adds 'DONE' to end of their item.
    def item_mark_complete(self):

        # Prompt for list item #
        to_checkoff = input("Which Item #?")

        # Check for digit.
        if not to_checkoff.isdigit():
            print('invalid list option')

        # Get the value at the line item number.
        else:
            to_checkoff = int(to_checkoff)
            self.todo_items[to_checkoff - 1].done = True
            self.print_todo_list()
            

    def print_todo_list(self):
        os.system("clear")
        print('To Do')

        i = 0
        while i < len(self.todo_items):
            each_item = self.todo_items[i]

            # Print the item number and title value.
            print('{} {}'.format(i + 1, each_item.print_item()))
            i = i + 1
