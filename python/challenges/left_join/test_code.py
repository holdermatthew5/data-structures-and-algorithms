import pytest
from linked_list import Node, LinkedList
from hashtable import Hash
from code import left_join

def test_left_join():
    pass

@pytest.fixture
def left():
    h = Hash()
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    return h

@pytest.fixture
def right():
    h = Hash()
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    return h

@pytest.fixture
def result():
    h = Hash()
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    h.add('', '')
    return h