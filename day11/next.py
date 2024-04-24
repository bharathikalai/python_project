class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#creatingnode
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#linking nodes
node1.next = node2
node2.next = node3

#traversing and printing the linked list
current_node = node1

while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
    print("current_node",current_node)
