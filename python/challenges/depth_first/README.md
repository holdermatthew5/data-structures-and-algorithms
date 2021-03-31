**Author:** Matthew Holder
**Version:** 0.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/45#issue-609438712)

# Depth First Graph traversal

## Problem Domain:

Conduct a depth first preorder traversal on a graph.

## Description:

The `depth_first` function takes in an adjacency_list as a graph (and an optional index from which to start that defaults to 0) and returns a list of the values of each node as they're discovered in a depth_first traversal.
- It starts by assigning a root node from which to start the depth_first traversal.
- It then continues to recursively move to any node that isn't in the visited list and appends it to the visited list.
- Finally when all available nodes have been visited it returns a list_comprehension list of the values of each node in the visited list.

### Developers Notes:

You might be interested in knowing that the order in which you create your edges does matter in testing. Using lists to hold each nodes edges means that when we explore a nodes edges they come in the order they're appended to that list, so you need to account for that when creating your expected value in testing. Having a drawing in the lab assignment helped to visualize this, so I added it as `graph.jpg`. The main code to pay attention to for this is the pytest fixture in `test_depth_first.py`.