class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}

    def add_vertex(self, vertex):
        if len(self.vertices) < self.num_vertices:
            self.vertices[vertex] = len(self.vertices)
        else:
            print("Graph: Cannot add more vertices than the initialized number.")

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.vertices[vertex1]
            index2 = self.vertices[vertex2]
            self.adj_matrix[index1][index2] = 1
            self.adj_matrix[index2][index1] = 1  # Fixing the typo for undirected graph
        else:
            print("Graph: One or both vertices not found in graph.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.vertices[vertex1]
            index2 = self.vertices[vertex2]
            self.adj_matrix[index1][index2] = 0
            self.adj_matrix[index2][index1] = 0
        else:
            print("Graph: One or both vertices not found in graph.")

    def __str__(self):
        result = "Vertices: " + str(list(self.vertices.keys())) + "\n"
        result += "Adjacency Matrix:\n"
        for row in self.adj_matrix:
            result += ' '.join(map(str, row)) + "\n"
        return result


# Example usage
if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)
    
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    
    print(graph)  # This will print the adjacency matrix and vertices once
    # graph.display()  # Remove or comment out this line to avoid duplicate output
