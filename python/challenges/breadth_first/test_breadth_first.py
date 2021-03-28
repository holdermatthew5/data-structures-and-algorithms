import pytest
from breadth_first import Node, Edge, Graph

def test_breadth_first(graph):
    assert graph.breadth_first('a') == [graph.adjacency_list[0], graph.adjacency_list[1], graph.adjacency_list[2], graph.adjacency_list[3]]

@pytest.fixture
def graph():
    graph = Graph()
    graph.adjacency_list.append(Node('a'))
    graph.adjacency_list.append(Node('b'))
    graph.adjacency_list.append(Node('c'))
    graph.adjacency_list.append(Node('d'))
    graph.addEdge('a', 'b', 1)
    graph.addEdge('a', 'c', 2)
    graph.addEdge('c', 'd', 3)
    graph.addEdge('d', 'b', 4)
    return graph