**Author:** Matthew Holder
**Version:** 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/35#issue-570044370)

Problem Domain:

I would like a function that takes in a k-ary and returns a new k-ary of the same shape.
In this new k-ary each node value should be altered, so that if it's divisible by 3 it becomes Fizz, if it's divisible by 5 it becomes Buzz, if it's divisible by both it becomes FizzBuzz and if it's not divisible by either it is simply converted to a string.

Description:

Node:
- The Node class instantiates a node object with .value equaling None until you give it a reference value and .n equaling an empty list until it's filled with new nodes.
KaryTree:
- The KaryTree class creates a k-ary tree object with .tree equaling a node.
FizzBuzzTree:
- The FizzBuzzTree function takes in a k-ary tree and returns a new tree with values altered according to problem domain.