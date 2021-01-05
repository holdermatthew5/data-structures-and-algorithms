import pytest
from ll_zip import LinkedList, Node, zipLists

def test_fixture_one(list_one):
    """
        tests first fixture alone to make sure it's working.
    """
    head = list_one.head
    assert head.value == 'a'

def test_fixture_two(list_two):
    """
        tests second fixture alone to make sure it's working.
    """
    head = list_two.head
    assert head.value == 'b'

def test_base_zip(list_one, list_two):
    """
        tests zip function with no edge cases.
    """
    returned = zipLists(list_one, list_two)
    result = returned.__str__()
    assert result == 'a -> b -> c -> d -> e -> f -> g -> h'

def test_zip_edge_one(long_list, list_two):
    """
        tests zip function when list one is longer than list two.
    """
    returned = zipLists(long_list, list_two)
    result = returned.__str__()
    assert result == 'a -> b -> c -> d -> e -> f -> g -> h -> i'

def test_zip_edge_two(long_list, list_two):
    """
        tests zip function when list two is longer than list one.
    """
    returned = zipLists(list_two, long_list)
    result = returned.__str__()
    assert result == 'b -> a -> d -> c -> f -> e -> h -> g -> i'

@pytest.fixture
def list_one():
    lists = LinkedList()
    lists.insert('g')
    lists.insert('e')
    lists.insert('c')
    lists.insert('a')
    return lists

@pytest.fixture
def list_two():
    lists = LinkedList()
    lists.insert('h')
    lists.insert('f')
    lists.insert('d')
    lists.insert('b')
    return lists

@pytest.fixture
def long_list():
    lists = LinkedList()
    lists.insert('i')
    lists.insert('g')
    lists.insert('e')
    lists.insert('c')
    lists.insert('a')
    return lists
