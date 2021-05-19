import pytest
from depth_first import depth_first, Graph, Edge, Node

def test_depth_first_from0(graph):
    assert depth_first(graph.adjacency_list) == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']

def test_depth_first_from4(graph):
    assert depth_first(graph.adjacency_list, 4) == ['E', 'D', 'H', 'F', 'A', 'B', 'C', 'G']

def test_depth_first_from5(graph):
    assert depth_first(graph.adjacency_list, 5) == ['F', 'H', 'D', 'E', 'A', 'B', 'C', 'G']

@pytest.fixture
def graph():
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')
    graph.addNode('G')
    graph.addNode('H')
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.addEdge('C', 'G')
    graph.addEdge('G', 'C')
    graph.addEdge('C', 'D')
    graph.addEdge('D', 'E')
    graph.addEdge('E', 'D')
    graph.addEdge('D', 'H')
    graph.addEdge('H', 'D')
    graph.addEdge('B', 'A')
    graph.addEdge('B', 'D')
    graph.addEdge('A', 'D')
    graph.addEdge('D', 'A')
    graph.addEdge('H', 'F')
    graph.addEdge('F', 'H')
    graph.addEdge('F', 'D')
    graph.addEdge('D', 'H')
    return graph