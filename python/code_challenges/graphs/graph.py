from code_challenges.stacks_and_queues.queue import Queue

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
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return list(self.adjacency_list[vertex])

    def size(self):
        return len(self.adjacency_list.keys())

    def breadth_first(self, node):
        queue = Queue()
        queue.enqueue(node)
        vertices = []
        while not queue.is_empty():
            current = queue.dequeue()
            if current.value not in vertices:
                vertices.append(current.value)
            for vertex in self.adjacency_list[current]:
                if vertex.vertex.value not in vertices:
                    queue.enqueue(vertex.vertex)
        return vertices


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
