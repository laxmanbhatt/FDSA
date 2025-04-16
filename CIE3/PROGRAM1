class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, v, w):
        if v not in self.adjacency_list:
            self.add_vertex(v)
        if w not in self.adjacency_list:
            self.add_vertex(w)
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)

    def remove_edge(self, v, w):
        if v in self.adjacency_list and w in self.adjacency_list[v]:
            self.adjacency_list[v].remove(w)
        if w in self.adjacency_list and v in self.adjacency_list[w]:
            self.adjacency_list[w].remove(v)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        return []

    def __str__(self):
        return str(self.adjacency_list)

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B')
g.add_vertex('C')
g.add_edge('A', 'C')

print("Graph:", g)

g.add_edge('B', 'C')
print("After adding edge B-C:", g)

print("Neighbors of A:", g.get_neighbors('A'))
print("Neighbors of B:", g.get_neighbors('B'))
