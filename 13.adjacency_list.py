# Program: Graph Operations using Adjacency List
# 1. Find adjacent nodes
# 2. Find degree, indegree, outdegree of vertices

class Graph:
    def __init__(self):
        # Adjacency list representation
        self.adj_list = {}

    # Add edge to the graph (directed or undirected)
    def add_edge(self, u, v, directed=False):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        if not directed:  # If undirected graph, add reverse edge too
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append(u)

    # Display adjacency list
    def display(self):
        print("\nGraph Adjacency List:")
        for node, neighbors in self.adj_list.items():
            print(f"{node} → {neighbors}")

    # Find adjacent nodes of a given node
    def find_adjacent(self, node):
        if node in self.adj_list:
            return self.adj_list[node]
        else:
            return []

    # Find degree, indegree, and outdegree
    def find_degrees(self, node, directed=False):
        if not directed:
            # For undirected graphs: degree = number of adjacent nodes
            degree = len(self.adj_list.get(node, []))
            return {"degree": degree, "indegree": degree, "outdegree": degree}
        else:
            # For directed graphs
            outdegree = len(self.adj_list.get(node, []))
            indegree = 0
            for v in self.adj_list:
                if node in self.adj_list[v]:
                    indegree += 1
            degree = indegree + outdegree
            return {"degree": degree, "indegree": indegree, "outdegree": outdegree}


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    g = Graph()

    print("=== Graph using Adjacency List ===")
    n = int(input("Enter number of edges: "))

    directed = input("Is the graph directed? (y/n): ").lower() == 'y'

    print("Enter edges (e.g., 1 2 means edge from 1 to 2):")
    for _ in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v, directed)

    g.display()

    # 1. Find adjacent nodes for specific vertices
    print("\n1. Adjacent Nodes:")
    for node in [1, 6, 3]:
        print(f"Adjacent to node {node}: {g.find_adjacent(node)}")

    # 2. Find degree, indegree, and outdegree
    print("\n2. Degree Information:")
    vertex = int(input("Enter vertex to find degree info: "))
    degree_info = g.find_degrees(vertex, directed)
    print(f"Vertex {vertex} → {degree_info}")
