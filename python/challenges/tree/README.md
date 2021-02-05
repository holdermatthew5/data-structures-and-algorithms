**Author:** Matthew Holder
**Version:** 0.1.2

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/33#issue-568099014)

# Implementation: Trees

## Problem Domain:

I would like a Node class which instantiates nodes to fit a binary tree. I would like a BinaryTree class which has methods preOrder, inOrder and postOrder which print the values of the nodes in the tree in their own orders. I would like a BinarySearchTree class which has methods add (adds node to proper place) and contains (returns True if a value is present in the tree at least once). I would like to be able to find the largest value in a Binary Tree.

## Description:

Node:
- Has self.value, self.left and self.right values and is used to hold values in a tree as well as carry references to other Node instances.
BinaryTree:
- preOrder:
  - Returns a string containing all values in a tree in the following order:
  ```
        |a|
    |b|     |c|
  |d| |e| |f|
  returns a b d e c f
  ```
- inOrder:
  - Returns a string containing all values in a tree in the following order:
  ```
        |a|
    |b|     |c|
  |d| |e| |f|
  returns d e b a f c
  ```
- postOrder:
  - Returns a string containing all values in a tree in the following order:
  ```
        |a|
    |b|     |c|
  |d| |e| |f|
  returns d e b f c a
- find_maximum_binary_tree:
  - Returns the highest value in it's own BinaryTree.
  ```
        |1|
    |2|     |3|
  |4| |5| |6|
  returns 6
  ```
- breadth_first:
  - Returns a string of the values of each node in the tree in breadth first order.
  ```
         |a|
    |b|      |c|
  |d| |e|  |f|
  returns 'A => B => C => D => E => F'
  ```

BinarySearchTree:
- add:
  - Adds a new node to the tree in the proper location.
- contains
  - Returns True if the tree contains a given value at least once.