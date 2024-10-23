class Vertex:
    def __init__(self, data):
        # Vertex data (identifier)
        self.data = data
        # Adjacency list to store connected vertices
        self.adjacencies = []

    def add_adjacency(self, other_vertex):
        # Add an edge (adjacent vertex) if it's not already in the adjacency list
        if other_vertex not in self.adjacencies:
            self.adjacencies.append(other_vertex)

    def __str__(self):
        # Representation of the vertex and its adjacent vertices
        adjacent_data = [str(vertex.data) for vertex in self.adjacencies]
        return f"Vertex({self.data}): Adjacent to -> {', '.join(adjacent_data)}"


class Graph:
    def __init__(self):
        # Dictionary to hold all vertices in the graph, key is vertex data
        self.vertices = {}

    def add_vertex(self, data):
        # Add a vertex with the given data if it doesn't already exist
        if data not in self.vertices:
            self.vertices[data] = Vertex(data)

    def add_edge(self, from_data, to_data):
        # Ensure both vertices exist, and then create an edge from one to the other
        if from_data not in self.vertices:
            self.add_vertex(from_data)
        if to_data not in self.vertices:
            self.add_vertex(to_data)

        # Add the adjacency from 'from_data' to 'to_data'
        self.vertices[from_data].add_adjacency(self.vertices[to_data])

    def has_vertex(self, data):
        # Return True if the vertex exists in the graph, else False
        return data in self.vertices

    def get_vertex(self, data):
        # Retrieve a vertex by its data, or return None if it doesn't exist
        return self.vertices.get(data, None)

    def __str__(self):
        # Return a string representation of the whole graph
        return "\n".join([str(vertex) for vertex in self.vertices.values()])


# Example Usage
if __name__ == "__main__":
    g = Graph()
    
    # Adding vertices
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    # Adding edges
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    
    # Check if a vertex exists
    print("Does vertex 1 exist?", g.has_vertex(1))  # True
    print("Does vertex 4 exist?", g.has_vertex(4))  # False
    
    # Search for a vertex
    v1 = g.get_vertex(1)
    if v1:
        print("Vertex 1 found:", v1)

    # Print the whole graph
    print("\nGraph structure:")
    print(g)
