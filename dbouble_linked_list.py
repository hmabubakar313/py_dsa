class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, new_data):
        new_node =Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAtLast(self,new_data):
        new_node = Node(new_data)  # Create a new node with the data
        if self.head is None:  # If the list is empty, new node becomes the head
            self.head = new_node
            return
        curr = self.head
        if curr is not None:
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data}", end=' <--> ')
            curr = curr.next
        print("None")


ll = LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtLast(19)
ll.print_list()
