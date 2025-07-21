class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp.next
    
    def enqueue(self, value):
        if self.last is None:
            new_node = Node(value)
            self.last = new_node
            self.first = new_node
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.last is None:
            return None
        temp = self.first
        if self.length == 1:
            self.last = None
            self.first = None
            return temp
        self.first = self.first.next
        temp.next = None
        i -= 1
        return temp
        