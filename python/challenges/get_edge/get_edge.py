def get_edge(graph, li):
    """
    This is intended to be a lead function in a recursive function which collects the weights of edges if they match the path the list is looking for.
    """
    total = 0
    for node in graph.adjacency_list:
        if node.value == li[0]:
            total += traverse(node)

def traverse(node):
    """
    This is the supporting function to get_edge. It handles recursion after the starting point is found.
    """
    for edge1 in node.edges:
        if edge1.neighbor.value == li[1]:
            total += edge1.weight
            for edge2 in edge1.edges:
                if edge2.neighbor.value == li[2]:
                    total += edge2.weight


class Graph():
    def __init__(self):
        self.adjacency_list = []

    def addNode(self, value):
        node = Node(value)
        self.adjacency_list.append(node)
        return node

    def addEdge(self, _from, to, weight=None):
        for node in self.adjacency_list:
            if node.value == _from:
                origin = node
            if node.value == to:
                neighbor = node
        edge = Edge(neighbor)
        origin.edges.append(edge)

    def getNodes(self):
        if self.adjacency_list ==[]:
            return None
        else:
            return self.adjacency_list

    def getNeighbors(self, value):
        if self.adjacency_list ==[]:
            return None
        for n in self.adjacency_list:
            if n.value == value:
                node = n
        result = []
        for edge in node.edges:
            result.append((edge, edge.weight))
        return result

    def size(self):
        return len(self.adjacency_list)

class Node():
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge():
    def __init__(self, neighbor, weight=None):
        self.weight = weight
        self.neighbor = neighbor