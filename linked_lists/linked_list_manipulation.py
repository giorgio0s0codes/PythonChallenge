class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def harcore_pop(self, value):

        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        current = self.head

        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            return False 
        
        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        return True

    def endoline_pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed = self.tail
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return removed
    
    def pop_first(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        removed.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return removed

    def get(self, index):
        if index < 0 or index >= self.length:
           return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        nod2mod = self.get(index)
        if nod2mod:
            nod2mod.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def print_list(self):
        current = self.head
        while current is not None:
            print (current.value)
            current = current.next


my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

