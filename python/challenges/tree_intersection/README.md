**Author:** Matthew Holder
**Version:** 0.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/40#issue-596259747)

## Problem Domain:

Find common values in 2 binary trees.

## Description:

The `intersection` function takes in 2 trees, uses recursion to travel through the trees simultaneously, and returns one list containing all values that both trees share.

This function makes use of two nested traversal methods to allow it to travel to branches that don't exist in the other tree.