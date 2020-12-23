Author: Matthew Holder

Version: 0.1.3

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/24#issue-544593563)

## Problem Domain:
    I want to be able to create a singly linked list, add nodes to the head of that linked list, find whether or not a node exists in that linked list by checking all nodes values and returning true if it does and false if it doesn't, and retrieve a string containing all values of all nodes in that linked list.

## Description:
    Components:
      - linked_list class
        - insert method
        - includes method
        - str method
      - Node class
    Use:
      - To create a linked list, assign it to a variable by calling the constructor as shown:
        - `my_linked_list = linked_list()`. No arguments are needed.

      - To add a node call the insert method on you newly created list as shown:
        - `my_linked_list.insert(value)` where 'value' is the value intended to be held by the node (nodes are automatically created in this method so there is no need to use the Node class).

      - To check the existence of a node (returns True if it exists in the list and False if it doesn't) call the includes method as shown:
        - `my_linked_list.includes(value)` where 'value' is the value held by the desired node.

      - To retrieve a string containing the values of all nodes present in the list call the str or __str__ method as shown:
        - `my_linked_list.str()` or `my_linked_list.__str__()`. No arguments needed.