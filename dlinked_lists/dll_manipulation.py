class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.length += 1
        return True
    
    def pop(self):
        if self.head == 1:
            self.head = self.tail = None
            i -= 1
            return None
        if self.head:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            i -= 1
            return temp
        return None
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head 
        if self.head == 1:
            self.head = self.tail = None
            return temp
        
        temp = self.head 
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index-1):
                temp = temp.prev
        
        return temp
    
    def set_value(self, index, value):
        nod2mod = self.get(index)
        if nod2mod == None:
            return False
        nod2mod.value = value
        return True

            

my_doubly_linked_list = DoublyLinkedList(77)
my_doubly_linked_list.print_list()