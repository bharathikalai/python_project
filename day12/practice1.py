class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class NewList:
    def __init__(self):
        self.head = None
    def add_name(self,name):
        new_name = Node(name)
        new_name.next = self.head
        self.head = new_name
        
    def display_list(self):
        display = self.head
        while display:
            print (display.data)
            display = display.next

names = NewList()

names.add_name("Alice")
names.add_name("bob")
names.add_name("charlie")


names.display_list()