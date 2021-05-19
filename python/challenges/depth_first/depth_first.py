def depth_first(graph, index = 0):
    root = graph[index]
    print([node.value for node in graph])
    visited = []
    def traverse(node):
        nonlocal visited
        if node not in visited:
            visited.append(node)
            if len(node.edges) > 0:
                for edge in node.edges:
                    if edge.neighbor not in visited:
                        traverse(edge.neighbor)
    traverse(root)
    return [node.value for node in visited]

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

if __name__ == '__main__':
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
    graph.addEdge('C', 'B')
    graph.addEdge('B', 'D')
    graph.addEdge('D', 'E')
    graph.addEdge('E', 'D')
    graph.addEdge('D', 'H')
    graph.addEdge('H', 'D')
    graph.addEdge('B', 'A')
    graph.addEdge('A', 'D')
    graph.addEdge('D', 'A')
    graph.addEdge('H', 'F')
    graph.addEdge('F', 'H')
    graph.addEdge('F', 'D')
    graph.addEdge('D', 'H')
    print(depth_first(graph.adjacency_list, 5))
    print(['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F'])