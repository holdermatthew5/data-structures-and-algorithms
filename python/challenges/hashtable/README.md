**Author:** Matthew Holder
**Version:** 0.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/38#issue-592775476)

# Hashtables

## Problem Domain

Build a Hash class which instantiates a hash table. This class should have add, get, contains, and get_hash methods.

## Description

Hash - Creates a hash table of a default size 1024 which can be increased or decreased by passing in the new size an an int when calling `Hash()`.
- add O(1) - adds a key value pair to the linked list at the hash index of the hash table as the `.data` of a node.
- get O(1) - returns the value of the key/value pair whose key matches a given key.
- contains O(n) - returns a bollean value declaring whether or not the hashtable contains a given key.
- get_hash O(1) - takes in a string a returns the sum of the ascii values of each of the strings characters as an index for the other methods.