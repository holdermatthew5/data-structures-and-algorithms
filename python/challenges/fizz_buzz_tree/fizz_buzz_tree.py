class Node:
    def __init__(self, value = None, n = []):
        self.value = value
        self.n = n
    
class KaryTree:
    def __init__(self, node=None):
        self.tree = node

def FizzBuzzTree(tree):
    new = KaryTree(Node(tree.tree.value))
    def traverse(node, node2):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node2.n.append(Node('FizzBuzz'))
        elif node.value % 3 == 0:
            node2.n.append(Node('Fizz'))
        elif node.value % 5 == 0:
            node2.n.append(Node('Buzz'))
        else:
            node2.n.append(Node(str(node.value)))
        for i in range(len(node.n)):
            print('a', node.value, 'b', node2.value)
            traverse(node.n[2], node2.n[2])
    traverse(tree.tree, new.tree)
    return new