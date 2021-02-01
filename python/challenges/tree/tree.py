class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def preOrder(self):
        string = ''
        def traverse(root):
            nonlocal string
            string = f'{string} {root.value}'
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return string

    def inOrder(self):
        string = ''
        def traverse(root):
            nonlocal string
            if root.left:
                traverse(root.left)
            string = f'{string} {root.value}'
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return string

    def postOrder(self):
        string = ''
        def traverse(root):
            nonlocal string
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            string = f'{string} {root.value}'
        traverse(self.root)
        return string

    def find_maximum_binary_tree(self):
        max_value = 0
        def traverse(root):
            nonlocal max_value
            if root.value > max_value:
                max_value = root.value
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return max_value

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        def traverse(root, value):
            print(root.value)
            if not root.left:
                root.left = Node(value)
            else:
                traverse(root.left, value)
            if not root.right:
                root.right = Node(value)
            else:
                traverse(root.right, value)
        traverse(self.root, value)

    def contains(self, value):
        response = False
        def helper(root, value):
            def traverse(root, value):
                print(root.value, value)
                if root.value == value:
                    nonlocal response
                    response = True
                if root.left:
                    traverse(root.left, value)
                if root.right:
                    traverse(root.right, value)
            traverse(root, value)
        helper(self.root, value)
        return response