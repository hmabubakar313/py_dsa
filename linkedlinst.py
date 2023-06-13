class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None        
    
    
    def inser_at_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    def inser_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            print("Node is inserted")
            return
        
        counter = self.head
        while counter.next:
            counter = counter.next
        counter.next = Node(data)
        print("Node is inserted")
    
    
    
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(count)
        return count
    
    
    
    def remove_at(self,index):
        print("Remove at index")
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 0
        itr = self.head
        while itr.next:
            if counter == index - 1:
                print("Node is removed")
                itr.next = itr.next.next
                break
            itr = itr.next
            counter += 1
            
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.inser_at_end(data)
        print(self.printList())
    print("List is inserted")
        
        
        
            
        
    
    def printList(self):
        if self.head is None:
            print("List is empty")
        count = ''
        temp = self.head
        while temp:
            count += str(temp.data) + '-->'
            temp = temp.next
        print(count)
    

if __name__=='__main__':
    ll = LinkedList()
    ll.inser_at_begin(10)
    ll.inser_at_begin(20)
    ll.inser_at_begin(30)
    ll.inser_at_end(40)
    ll.printList()
    ll.get_length()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.remove_at(2)
    ll.printList()
    
    