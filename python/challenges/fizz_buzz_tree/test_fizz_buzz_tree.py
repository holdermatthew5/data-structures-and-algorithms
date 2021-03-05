import pytest
from fizz_buzz_tree import Node, KaryTree, FizzBuzzTree

def test_tree(tree):
    assert tree.root

def test_node(tree):
    assert tree.root.value == 1

def test_fizz_buzz1(tree):
    assert FizzBuzzTree(tree) != tree

def test_fizz_buzz2(tree):
    assert FizzBuzzTree(tree).root.right.value == 'Fizz'

def test_fizz_buzz3(tree):
    assert FizzBuzzTree(tree).root.left.right.value == 'Buzz'

def test_fizz_buzz4(tree):
    assert FizzBuzzTree(tree).root.right.left.value == 'FizzBuzz'

def test_fizz_buzz5(tree):
    assert type(FizzBuzzTree(tree).root.value) == str


@pytest.fixture
def tree():
    tree = KaryTree(Node(1))
    root = tree.root
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(15)
    return tree