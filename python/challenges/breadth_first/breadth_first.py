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

    def breadth_first(self, value):
        visited = []
        def add_to_visited(value):
            for node in self.adjacency_list:
                if node.value == value:
                    nonlocal visited
                    if node not in visited:
                        visited.append(node)
                    for edge in node.edges:
                        if edge.neighbor not in visited:
                            visited.append(edge.neighbor)
                            add_to_visited(edge.neighbor)
                        # else:
                        #     return
        return visited

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