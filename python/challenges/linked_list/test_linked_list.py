import pytest
from linked_list import LinkedList, Node

def test_linked_list(linked_list):
    assert linked_list

def test_insert(linked_list):
    assert linked_list.head.value == 'd'

def test_next(linked_list):
    assert linked_list.head.next.value == 'c'

def test_includes_true(linked_list):
    assert linked_list.includes('a')

def test_includes_false(linked_list):
    assert not linked_list.includes('e')

def test_string(linked_list):
    assert linked_list.__str__() == 'd -> c -> b -> a'

@pytest.fixture
def linked_list():
    new_linked_list = LinkedList()
    new_linked_list.insert('a')
    new_linked_list.insert('b')
    new_linked_list.insert('c')
    new_linked_list.insert('d')
    return new_linked_list