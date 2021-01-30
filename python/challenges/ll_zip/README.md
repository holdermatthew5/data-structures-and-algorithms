Author: Matthew Holder

Version: 1.0.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/25#issue-548704764)

## Problem Domain
    I want to be able to combine 2 singly linked lists in a zipping fashion. If the first list contains node values 1, 3, 5, and 7 and the second list contains node values 2, 4, 6, and 8 the function should return a singly linked lists with node values 1, 2, 3, 4, 5, 6, 7, and 8.

## Description:
    Original Components:
      - zipLists function
    Use:
      - To use the zipLists function assign its instance to a variable passing in 2 linked lists as arguments. This can be done with the following code:
        - `variable = zipLists(first_list, second_list)`
      - After this `variable` will hold one singly linked list containing all nodes from both previous lists as described in the problem domain.