"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head is None:
            self.head = new_element
            return
        
        while current.next:
            current = current.next
        current.next = new_element
        return
            
    def get_position(self, position):
        current = self.head
        while current:
            if position == 1:
                return current
            current = current.next
            position -= 1
        return current
    
    # def insert(self, new_element, position):
    #     """Insert a new node at the given position.
    #     Assume the first position is "1".
    #     Inserting at position 3 means between
    #     the 2nd and 3rd elements."""
    #     pass
    
    
    def delete(self, value):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        
        
        
        
    
    
    def print_list(self):
        current = self.head
        lstr = ''
        counter = 0
        while current.next:
            lstr += str(current.value) + '->'
            current = current.next
            
        counter += 1
        print(lstr + str(current.value))
            
        
        
    
           
            
            
            
                        
    

if __name__=='__main__':

    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    # ll.delete(1)
    ll.print_list()
    ll.delete(0)    
    ll.print_list()
    
    

    # Test get_position
    # Should print 3
    # print ll.head.next.next.value
    # Should also print 3
    # print ll.get_position(3).value

    # Test insert
    # ll.insert(e4,3)
    # Should print 4 now
    # print ll.get_position(3).value

    # Test delete
    # ll.delete(1)
    # Should print 2 now
    # print ll.get_position(1).value
    # Should print 4 now
    # print ll.get_position(2).value
    # Should print 3 now
    # print(ll.get_position(3).value)
    # print ll.get_position(3).value