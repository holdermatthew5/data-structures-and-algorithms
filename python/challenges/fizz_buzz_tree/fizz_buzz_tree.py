class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
class KaryTree:
    def __init__(self, node=None):
        self.root = node

def FizzBuzzTree(tree):
    new = KaryTree(Node(tree.root.value))
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return 'FizzBuzz'
        elif value % 3 == 0:
            return 'Fizz'
        elif value % 5 == 0:
            return 'Buzz'
        else:
            return str(value)
    def traverse(root1, root2):
        if root1.left:
            root2.left = Node(str(fizz_buzz(root1.left.value)))
            traverse(root1.left, root2.left)
        if root1.right:
            root2.right = Node(str(fizz_buzz(root1.right.value)))
            traverse(root1.right, root2.right)
    traverse(tree.root, new.root)
    return new

if __name__ == '__main__':
    tree = KaryTree(Node(1))
    root = tree.root
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(15)
    print(FizzBuzzTree(tree).root.value)