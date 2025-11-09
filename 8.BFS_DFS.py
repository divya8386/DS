# Program: Graph Traversal using BFS (Adjacency List) and DFS (Adjacency Matrix)

from collections import deque

# ---------- BFS using Adjacency List ----------
def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            # Add all unvisited neighbors
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return bfs_order


# ---------- DFS using Adjacency Matrix ----------
def dfs(matrix, start_index, nodes):
    visited = [False] * len(nodes)
    dfs_order = []

    def dfs_recursive(v):
        visited[v] = True
        dfs_order.append(nodes[v])
        for i in range(len(matrix[v])):
            if matrix[v][i] == 1 and not visited[i]:
                dfs_recursive(i)

    dfs_recursive(start_index)
    return dfs_order


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # Define popular locations (graph nodes)
    locations = ["A", "B", "C", "D", "E"]

    # Adjacency List for BFS
    adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["B", "D"]
    }

    # Adjacency Matrix for DFS (same graph)
    adj_matrix = [
        # A  B  C  D  E
        [0, 1, 1, 0, 0],  # A
        [1, 0, 0, 1, 1],  # B
        [1, 0, 0, 1, 0],  # C
        [0, 1, 1, 0, 1],  # D
        [0, 1, 0, 1, 0]   # E
    ]

    start_location = "A"

    # Perform BFS
    print("BFS Traversal (using Adjacency List):")
    bfs_result = bfs(adj_list, start_location)
    print(" → ".join(bfs_result))

    # Perform DFS
    print("\nDFS Traversal (using Adjacency Matrix):")
    start_index = locations.index(start_location)
    dfs_result = dfs(adj_matrix, start_index, locations)
    print(" → ".join(dfs_result))
