# item.py - Upper-Polo To Do List App

# This module defines the Item class.
# Each new todo entry is an instance of Item.
# Item accepts a title, which is the text for the entry.
# Item has a 'done' value for marking as complete.

class Item:
    def __init__(self, title):
        self.title = title
        self.done = False
        # TODO: self.date
        # TODO: self.description

    def print_item(self):
        if self.done:
            return '{} (DONE)'.format(self.title)
        else:
            return '{}'.format(self.title)
