import pytest
from linked_list import Node, LinkedList
from hashtable import Hash
from code import left_join

def test_left_join():
    pass

@pytest.fixture
def left():
    h = Hash()
    h.add('xa', 'left1')
    h.add('wa', 'left2')
    h.add('va', 'left3')
    h.add('re', 'left4')
    h.add('tc', 'left5')
    return h

@pytest.fixture
def right():
    h = Hash()
    h.add('xa', 'right1')
    h.add('wa', 'right2')
    h.add('va', 'right3')
    h.add('re', 'right3')
    h.add('kl', 'right5')
    return h

@pytest.fixture
def result():
    h = Hash()
    h.add('xa', 'left1')
    h.add('wa', 'left2')
    h.add('va', 'left3')
    h.add('re', 'left4')
    h.add('tc', 'left5')
    return h