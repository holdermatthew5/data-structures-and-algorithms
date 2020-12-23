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

def test_append():
    appendList = LinkedList()
    appendList.insert("THR33")
    appendList.insert("TOO")
    appendList.insert("WON")
    appendList.append("FOR")
    actual = [appendList.head.nodeValue, appendList.head.nextNodeValue.nodeValue, appendList.head.nextNodeValue.nextNodeValue.nodeValue, appendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FOR"]
    assert actual == expected

def test_multiple_append():
    multipleAppendList = LinkedList()
    multipleAppendList.insert("THR33")
    multipleAppendList.insert("TOO")
    multipleAppendList.insert("WON")
    multipleAppendList.append("FOR")
    multipleAppendList.append("F1V3")
    actual = [multipleAppendList.head.nodeValue, multipleAppendList.head.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue, multipleAppendList.head.nextNodeValue.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FOR", "F1V3"]
    assert actual == expected

def test_insert_before_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("TOO", "INSERTER")
    actual = [insertBeforeList.head.nodeValue, insertBeforeList.head.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "INSERTER", "TOO", "THR33"]
    assert actual == expected

def test_insert_before_head_value():
    insertBeforeList = LinkedList()
    insertBeforeList.insert("THR33")
    insertBeforeList.insert("TOO")
    insertBeforeList.insert("WON")
    insertBeforeList.insertBefore("WON", "Z3R0")
    actual = [insertBeforeList.head.nodeValue, insertBeforeList.head.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nodeValue, insertBeforeList.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["Z3R0", "WON", "TOO", "THR33"]
    assert actual == expected

def test_insert_in_middle_value():
    insertToMiddle = LinkedList()
    insertToMiddle.insert("THR33")
    insertToMiddle.insert("TOO")
    insertToMiddle.insert("WON")
    insertToMiddle.insertAfter("WON", "FORE")
    actual = [insertToMiddle.head.nodeValue, insertToMiddle.head.nextNodeValue.nodeValue, insertToMiddle.head.nextNodeValue.nextNodeValue.nodeValue, insertToMiddle.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "FORE", "TOO", "THR33"]
    assert actual == expected

def test_insert_to_end_value():
    insertToEnd = LinkedList()
    insertToEnd.insert("THR33")
    insertToEnd.insert("TOO")
    insertToEnd.insert("WON")
    insertToEnd.insertAfter("THR33", "FORE")
    actual = [insertToEnd.head.nodeValue, insertToEnd.head.nextNodeValue.nodeValue, insertToEnd.head.nextNodeValue.nextNodeValue.nodeValue, insertToEnd.head.nextNodeValue.nextNodeValue.nextNodeValue.nodeValue]
    expected = ["WON", "TOO", "THR33", "FORE"]
    assert actual == expected

@pytest.fixture
def linked_list():
    new_linked_list = LinkedList()
    new_linked_list.insert('a')
    new_linked_list.insert('b')
    new_linked_list.insert('c')
    new_linked_list.insert('d')
    return new_linked_list