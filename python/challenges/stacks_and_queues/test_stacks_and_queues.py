import pytest
from stacks_and_queues import Node, Stack, Queue, InvalidOperationError

# Can successfully push onto a stack
def test_push():
    stack = Stack()
    stack.push('works')
    assert stack.top.value == 'works'

# Can successfully push multiple values onto a stack
def test_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top.value == 2 and stack.top.next.value == 1

# Can successfully pop off the stack
def test_pop():
    stack = Stack()
    stack.push('still here')
    stack.pop()
    assert stack.top == None

# Can successfully empty a stack after multiple pops
def test_pop_to_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty

# Can successfully peek the next item on the stack
def test_peek():
    stack = Stack()
    stack.push('works')
    assert stack.peek == 'works'

# Can successfully instantiate an empty stack
def test_stack():
    stack = Stack()
    assert stack.top == None

# Calling pop or peek on empty stack raises exception
def test_stack_exception():
    stack = Stack()
    exc = "Method not allowed on empty collection."
    with pytest.raises(InvalidOperationError) as error1:
        stack.peek()
    with pytest.raises(InvalidOperationError) as error2:
        stack.pop()
    assert str(error1.value) == exc and str(error2.value) == exc

# Can successfully enqueue into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue('works')
    assert queue.front.value == 'works' and queue.rear.value == 'works'

# Can successfully enqueue multiple values into a queue
def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.rear.value == 2 and queue.front.value == 1

# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    pass

# Can successfully peek into a queue, seeing the expected value
def test_peek():
    queue = Queue()
    queue.enqueue('works')
    assert queue.peek() == 'works'

# Can successfully empty a queue after multiple dequeues
def test_dequeue_to_empty():
    pass

# Can successfully instantiate an empty queue
def test_queue():
    queue = Queue()
    assert queue.front == None and queue.rear == None

# Calling dequeue or peek on empty queue raises exception
def test_queue_exception():
    queue = Queue()
    exc = "Method not allowed on empty collection."
    with pytest.raises(InvalidOperationError) as error1:
        queue.peek()
    assert str(error1.value) == exc