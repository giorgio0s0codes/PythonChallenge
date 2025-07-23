class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def _r_contains(self, current_node, value):
        if current_node is None:
            return None
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self._r_contains(current_node.left, value)
        if value > current_node.value:
            return self._r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self._r_contains(self.root, value)

    def _r_insert(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left.value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right.value)
        return current_node
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self._r_insert(self.root, value)

    def _r_delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.left.value:
            current_node.left = self._r_delete_node(current_node.left, value)
        elif value > current_node.right.value:
            current_node.right = self._r_delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            
        return current_node
    
    def r_delete_node(self, value):
        self.root = self._r_delete_node(self.root, value)

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)                
