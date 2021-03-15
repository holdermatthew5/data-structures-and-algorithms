import pytest
from hashtable import Hash
from linked_list import Node, LinkedList

# Adding a key/value to your hashtable results in the value being in the data structure

def test_add(h):
    passes = True
    for index in range(len(h.table)):
        if h.table[index]:
            if 'firstkey' not in [kv[0] for kv in h.table[index].display()]:
                passes = False
    assert passes

# Retrieving based on a key returns the value stored

def test_get(h):
    assert h.get('firstkey') == 'firstvalue'

# Successfully returns null for a key that does not exist in the hashtable

def test_get_null(h):
    assert h.get('secondkey') == None

# Successfully handle a collision within the hashtable

def test_add_collision(h):
    h.add('zzzzfaaa', 'testvalue')
    passes = False
    current = h.table[h.get_hash('zzzzfaaa')].head
    while current:
        if current.data[0] == 'zzzzfaaa':
            passes = True
        current = current.next
    assert passes

# Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_get_collision(h):
    h.add('zzzzfaaa','testvalue')
    assert h.contains('zzzzfaaa')

# Successfully hash a key to an in-range value

def test_get_hash(h):
    expected_range = h.size
    actual_hash = h.get_hash('supercalifragilisticexpialidocious')
    assert expected_range >= actual_hash

@pytest.fixture
def h():
    h = Hash()
    h.add('firstkey','firstvalue')
    return h