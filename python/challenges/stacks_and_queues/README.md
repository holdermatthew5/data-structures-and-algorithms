**Author:** Matthew Holder
**Version:** 0.1.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/26#issue-553957599)

## Stacks and Queues
Problem Domain:

    I would like to be able to create a Stack and use the standard (push, pop, peek, is_empty) methods.
    I would like to be able to create a Queue and use the standard (enqueue, dequeue, peek, is_empty) methods.

Description:

    Stack
      - .push() - Creates a node with a given value and inserts in into the top of the stack (takes one value argument).
      - .pop() - Removes the node from the top of the stack and returns it to the user (takes no arguments).
      - .peek() - Returns the value of the node at the top of the stack (takes no arguments).
      - .is_empty() - Returns boolean declaring whether or not the stack is empty (takes no arguments).
    
    Queue
      - .enqueue() - Creates a new node with a given value and adds it to the rear (.rear) of the queue (takes one value argument).
      - .dequeue() - Removes the node at the front (.front) of the queue and returns it to the user (takes no arguments).
      - .peek() - Returns the value of the node at the front of the queue (takes no arguments).
      - .is_empty() - Returns boolean declaring whether or not the queue is empty (takes no arguments).

Credits:
- Exception class copied from [class repo](https://github.com/codefellows/seattle-python-401n2/blob/main/class-10/demo/stacks_and_queues/stacks_and_queues.py).