import pytest
from linked_list import linked_list, Node

def test_linked_list():
    new_linked_list = linked_list()
    assert new_linked_list

def test_insert():
    new_linked_list = linked_list()
    new_linked_list.insert('a')
    assert new_linked_list.head.value == 'a'

def test_includes():
    new_linked_list = linked_list()
    new_linked_list.insert('a')
    assert new_linked_list.includes('a')

def test_string():
    new_linked_list = linked_list()
    new_linked_list.insert('a')
    new_linked_list.insert('b')
    new_linked_list.insert('c')
    new_linked_list.insert('d')
    assert new_linked_list.str() == 'a -> b -> c -> d'

@pytest.fixture