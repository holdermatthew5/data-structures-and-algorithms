import pytest
from linked_list import Node, LinkedList
from hashtable import Hash
from left_join import left_join

def test_left_join(left, right, known):
    result = left_join(left, right)
    result_values = []
    known_values = []
    for ll1 in result.table:
        if ll1 and ll1.head:
            current = ll1.head
            while current:
                result_values.append(current.data)
                current = current.next
    for ll2 in known.table:
        if ll2 and ll2.head:
            current = ll2.head
            while current:
                known_values.append(current.data)
                current = current.next
    assert result_values == known_values

def parse_h(h, key, value):
    for index in h.table:
        if index:
            current = index.head
            while current:
                if current.data[0] == value:
                    current.data.append(value)
                current = current.next

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
def known():
    h = Hash()
    h.add('xa', 'left1')
    h.add('wa', 'left2')
    h.add('va', 'left3')
    h.add('re', 'left4')
    h.add('tc', 'left5')
    parse_h(h, 'va', 'right3')
    # parse_h(h, '')
    return h