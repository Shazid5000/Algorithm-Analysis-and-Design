class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print(f"Vertex '{vertex}' already exists in the graph.")

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        else:
            print("One or both vertices not found in graph.")

    def __str__(self):
        result = ""
        for vertex in self.adj_list:
            result += f"{vertex}: {self.adj_list[vertex]}\n"
        return result


# Example usage
if __name__ == "__main__":
    graph = Graph()
    
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    
    print(graph)  # This will print the adjacency list once
