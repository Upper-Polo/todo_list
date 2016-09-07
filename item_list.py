# Upper-Polo To Do List App

# An Item object for each user entry to their todo list.

class ItemList:
    def __init__(self):
        self.todo_items = []

    def add(self, item):
        self.todo_items.append(item)
        

    def remove(self, item):
        # TODO: Check inputs
        
        self.todo_items.remove(item)    

