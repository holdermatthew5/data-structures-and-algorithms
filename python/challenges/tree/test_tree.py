import pytest
from tree import Node, BinaryTree, BinarySearchTree

# Can successfully instantiate an empty tree

def test_instance():
    tree = BinaryTree()
    assert isinstance(tree, BinaryTree)

# Can successfully instantiate a tree with a single root node

def test_single_root():
    tree = BinaryTree(Node('a'))
    assert isinstance(tree.root, Node) and tree.root.value == 'a'

# Can successfully add a left child and right child to a single root node

def test_add_children():
    tree = BinaryTree(Node('a'))
    tree.root.left = Node('b')
    tree.root.right = Node('c')
    assert tree.root.left.value == 'b' and tree.root.right.value == 'c'

# Can successfully return a collection from a preorder traversal

def test_preorder(tree):
    assert tree.preOrder() == ' A B D E C F'

# Can successfully return a collection from an inorder traversal

def test_inorder(tree):
    assert tree.inOrder() == ' D B E A F C'

# Can successfully return a collection from a postorder traversal

def test_postorder(tree):
    assert tree.postOrder() == ' D E B F C A'

# Can successfully add node to BinarySearchTree
def test_add(search):
    search.add('G')
    assert search.root.right.right.value == 'G'

# Can successfully return proper boolean depending on whether a given value is present
def test_contains(search):
    assert search.contains('F')

# Can successfully traverse a tree breadth first
def test_breadth_first(tree):
    assert tree.breadth_first() == 'A => B => C => D => E => F'

@pytest.fixture
def tree():
    tree = BinaryTree(Node('A'))
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree

@pytest.fixture
def search():
    tree = BinarySearchTree(Node('A'))
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree