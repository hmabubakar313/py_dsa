class Node:
    def __init__(self, data=None):
        print("Node function initialized!")
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        print("Linked function initialized!")
        self.head = head
        self.next = None
        
        
    def insert(self, data):
        print("Insert function initialized!")
        if self.head is None:
            self.head = Node(data)
            return
        else:
            




if __name__ == "__main__":
    ll = LinkedList()
    node = Node()
    print(ll.head)
    print(node.data)
    ll.insert(1)
    