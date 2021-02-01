import pytest
from queue_with_stacks import InvalidOperationError, PseudoQueue, Stack, Node

def test_stack():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as error:
        stack.peek()
    assert str(error.value) == "Method not allowed on empty collection."

def test_enqueue_empty():
    queue = PseudoQueue()
    queue.enqueue(Stack())
    with pytest.raises(InvalidOperationError) as error:
        queue.front.peek()
    assert str(error.value) == "Method not allowed on empty collection."

def test_enqueue_two():
    queue = PseudoQueue()
    queue.enqueue(Stack())
    queue.front.push('Front')
    queue.enqueue(Stack())
    queue.rear.push('Rear')
    assert queue.front.peek() == 'Front' and queue.rear.peek() == 'Rear'

def test_dequeue_empty():
    queue = PseudoQueue()
    with pytest.raises(InvalidOperationError) as error:
        queue.dequeue()
    assert str(error.value) == "Method not allowed on empty queue."
    
def test_dequeue_one():
    queue = PseudoQueue()
    queue.enqueue(Stack())
    queue.front.push('First')
    assert queue.dequeue().peek() == 'First'

def test_dequeue_two():
    queue = PseudoQueue()
    queue.enqueue(Stack())
    queue.front.push('First')
    queue.enqueue(Stack())
    queue.rear.push('Second')
    assert queue.dequeue().peek() == 'First' and queue.dequeue().peek() == 'Second'