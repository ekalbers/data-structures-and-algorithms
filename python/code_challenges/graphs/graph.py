class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start, end, weight=0):
        self.adjacency_list[end]
        self.adjacency_list[start].append(Edge(end, weight))

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list.keys())


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
