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
    
    def breadth_first(self):
        nodes = [self.root]
        string = ''
        def traverse(root):
            nonlocal nodes
            nonlocal string
            if root:
                if string == '':
                    string = root.value
                else:
                    string = f'{string} => {root.value}'
            if root.left:
                nodes.append(root.left)
            if root.right:
                nodes.append(root.right)
            if root.left:
                traverse(nodes.pop(0))
            if root.right:
                traverse(nodes.pop(0))
        traverse(nodes.pop(0))
        return string

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