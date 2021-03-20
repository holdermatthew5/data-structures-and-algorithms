import pytest
from tree_intersection import intersection
from tree import BinaryTree, Node

def test_intersection(tree1, tree2):
    assert intersection(tree1, tree2) == ['b', 'd', 'f']

def test_oneheavy_intersection(tree1, tree2):
    root = tree1.root.left
    root.left.left = Node('a2')
    root.left.right = Node('c2')
    root.right.left = Node('e2')
    root.right.right = Node('g2')
    print(intersection(tree1, tree2))
    assert intersection(tree1, tree2) == ['b', 'd', 'a2', 'c2', 'e2', 'g2', 'f']

def test_twoheavy_intersection(tree1, tree2):
    root = tree2.root.left
    root.left.left = Node('a1')
    root.left.right = Node('c1')
    root.right.left = Node('e1')
    root.right.right = Node('g1')
    print(intersection(tree1, tree2))
    assert intersection(tree1, tree2) == ['b', 'd', 'a1', 'c1', 'e1', 'g1', 'f']

@pytest.fixture
def tree1():
    tree = BinaryTree(Node('a1'))
    root = tree.root
    root.left = Node('b')
    root.right = Node('c1')
    root.left.left = Node('d')
    root.left.right = Node('e1')
    root.right.left = Node('f')
    root.right.right = Node('g1')
    return tree

@pytest.fixture
def tree2():
    tree = BinaryTree(Node('a2'))
    root = tree.root
    root.left = Node('b')
    root.right = Node('c2')
    root.left.left = Node('d')
    root.left.right = Node('e2')
    root.right.left = Node('f')
    root.right.right = Node('g2')
    return tree