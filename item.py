# Upper-Polo To Do List App


# An Item object for each user entry to their todo list.

class Item:
    def __init__(self, title):
        self.title = title
        self.done = False
        # self.date =

    def print_item(self):
        if self.done:
            return '{} (DONE)'.format(self.title)
        else:
            return '{}'.format(self.title)


    
