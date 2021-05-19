**Author:** Matthew Holder
**Version:** 0.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/43#issue-606866422)

## Problem Domain:

- Define a breadth_first traversal method that extends from the graph, takes in the value of a node, traverses all vertices in the order they're found and returns a list of visited nodes. No one node should be present in the returned list more than once.

## Description:

- Graph.breadth_first is a method which takes in the value of a node, finds the node it belongs to, visits all of its neighbors and recurses with each one adding each unvisited node to the return list as it's visited for the first time.