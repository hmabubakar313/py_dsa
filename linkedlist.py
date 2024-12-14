class Node:
    def __init__(self, value):  # Fixed typo in __init__
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAttheEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_data
            return -1

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end='-->')
            temp = temp.next
        print()

    def deleteAtEnd(self):
        if self.head is None:
            return 'Emptry lined list'
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return 'list is Empty'
        if self.head.next is None:
            self.head = None
            return -1
        temp = self.head
        while temp.next.next:





ll = LinkedList()
ll.insertAtBeginning(5)
ll.insertAtBeginning(7)
ll.insertAtBeginning(8)
ll.insertAttheEnd(10)
ll.deleteAtEnd()
ll.printList()
