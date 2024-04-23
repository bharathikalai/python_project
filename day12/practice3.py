class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class NameList:
    def __init__(self):
        self.head = None

    def add_name(self,name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
    def display_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    def search_name(self,name):
        serach_name = self.head

        while serach_name:
            if serach_name.data == name:
                print(f"name {name} found in the list")
                return
            serach_name = serach_name.next
        print(f"name {name } not found in the list")


names = NameList()

while True:
    print("\nName List Menu:")
    print("1. Add Name")
    print("2. View Names")
    print("3. Search Names")
    print("4. Exit")

    choice = input("enter your choice:")
    if choice == '1':
        name = input("enter name to add")
        names.add_name(name)
    elif choice == '2':
        names.display_list()

    elif choice == '3':
        name = input("enter name to search: ")
        names.search_name(name)

    elif choice == '4':
        print("exiting...")
        break
    else:
        print("invalid choice please choose again")