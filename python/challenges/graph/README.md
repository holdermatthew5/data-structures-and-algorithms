**Author:** Matthew Holder
**Version:** 0.1

[PR]()

## Problem Domain

- Implement a graph as an adjacency list. The graph should contain:
  - AddNode - Adds a node with a given value to the graph and returns the added node.
  - AddEdge - Takes in 2 nodes already in the graph and gives them an edge. The edge should also have a weight.
  - GetNodes - Returns all nodes in the graph as a collection (set, list or similar).
  - GetNeighbors - Returns a collection of the edges, with their weights, of a given node.
  - Size methods - Returns the total number of nodes in a graph.

## Notes:

- The default argument in `.getNeighbors` seems to be refusing to apply passed in arguments.