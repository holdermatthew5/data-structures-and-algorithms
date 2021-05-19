import pytest
from graph import Node, Edge, Graph

def test_node():
    assert Node('a').value == 'a'

def test_edge():
    edge = Edge(Node('a'), 4)
    assert edge.neighbor.value == 'a' and edge.weight == 4

def test_graph():
    assert Graph().adjacency_list == []

# A graph with only one node and edge can be properly returned
    # but the lab says to make it so both nodes have to exist in the graph already in order for an edge to be formed. I can return a graph with one node but not one node and an edge.
def test_one_node():
    graph = Graph()
    return graph.addNode('a')

# Node can be successfully added to the graph
def test_addNode(graph):
    assert graph.adjacency_list[0].value == 'a'

# An edge can be successfully added to the graph
def test_addEdge(graph):
    assert graph.adjacency_list[0].edges[0].neighbor.value == 'b' and graph.adjacency_list[1].edges[0].neighbor.value == 'a'

# A collection of all nodes can be properly retrieved from the graph
def test_getNodes(graph):
    assert graph.getNodes() == graph.adjacency_list

# An empty graph properly returns null
def test_empty_graph():
    assert Graph().getNodes() == None

# All appropriate neighbors can be retrieved from the graph
def test_getNeighbors(graph):
    assert graph.getNeighbors('a') == [(graph.adjacency_list[0].edges[0], graph.adjacency_list[0].edges[0].weight)] and graph.getNeighbors('b') == [(graph.adjacency_list[1].edges[0], graph.adjacency_list[1].edges[0].weight)]

# Neighbors are returned with the weight between nodes included
def test_weight(graph):
    assert graph.getNeighbors('a')[0][1] == 1

# The proper size is returned, representing the number of nodes in the graph
def test_size(graph):
    assert graph.size() == 2

@pytest.fixture
def graph():
    graph = Graph()
    graph.adjacency_list.append(Node('a'))
    graph.adjacency_list.append(Node('b'))
    graph.addEdge('a', 'b', 1)
    graph.addEdge('b', 'a', 2)
    return graph