class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkList:
    def __init__(self):
        self.head = None
    
    
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
            
    def print_list(self):
        cur = self.head
        counter =''
        while cur:
            counter = counter + str(cur.data) + '->'
            # print(cur.data)
            cur = cur.next
        print(counter)
    
    
    def append_at_last(self,data):
        cur = self.head
        counter = ''
        while cur.next:
            counter = counter + str(cur.data) + '->'
            cur = cur.next
        cur.next = Node(data)
        print(counter)
    
    
    def append_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print('printting from append_at_begining',self.head.data)
        
        
        
    def get_length(self):
        cur = self.head
        counter = 0
        while cur:
            counter += 1
            cur = cur.next
        print(cur.next.data)
        # print(counter)  
        
        
    # def append_at_index(self,index,data):
    #     # if index < 0 or index > self.get_length():
    #     #     raise Exception('Invalid Index')
        
    #     if index == 0:
    #         self.append_at_begining(data)
    #         return 
    #     elif index == self.get_length():
    #         self.append_at_last(data)
    #         return
    #     else:
    #         cur = self.head
    #         counter = 0
    #         while cur:
    #             print('counter before ++',counter)
    #             print('inside while loop')
    #             if counter == index:
    #                 new_node = Node(data)
    #                 new_node.next = cur.next
    #                 cur.next = new_node
    #                 print('counter',counter)
    #             counter += 1
            # break
            
        
            
            
    
  
                
        
        


if __name__ == '__main__':
    ll = LinkList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    # ll.print_list()
    ll.append_at_last(3)
    # ll.print_list()
    ll.append_at_begining(0)
    # ll.print_list()
    # ll.get_length()
    # ll.append_at_index(3,5)
    ll.print_list()