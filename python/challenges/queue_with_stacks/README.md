**Author:** Matthew Holder
**Version:** 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/27#issue-554628587)

Problem Domain:

    I would like to be able to create a stack queue which holds 2 stacks at a time and is capable of `enqueue` and `dequeue` methods.

Description:

    PseudoQueue() - Holds up to two stacks at a time.
      - enqueue() - Pushes one Stack into queue at a time. When empty the first stack is placed in `.front`. When front is taken places next stack in `.rear`. Raises `InvalidOperationError` when enqueued to full queue.
      - dequeue() - Pulls one stack from queue at a time. When full pulls from front, moves rear to front and reassigns rear to None. When half full pulls from front and reassigns front to None. Raises InvalidOperationError when dequeued from empty.

Credits:
    Stack - Copied from `../stacks_and_queues/stacks_and_queues.py`.
    Node - Copied from `../stacks_and_queues/stacks_and_queues.py`.
    InvalidOperationError - Copied from [Class Demo](https://github.com/codefellows/seattle-python-401n2/blob/main/class-10/demo/stacks_and_queues/stacks_and_queues.py)