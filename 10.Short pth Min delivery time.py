# Program: Pizza Delivery Optimization using Dijkstra's Algorithm

import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}  # adjacency list to store (neighbor, time)

    # Add edge between two locations
    def add_edge(self, u, v, time):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, time))
        self.adj_list[v].append((u, time))  # Assuming undirected graph (two-way roads)

    # Dijkstra's Algorithm to find shortest delivery times
    def dijkstra(self, start):
        min_heap = [(0, start)]  # (time, node)
        shortest_time = {node: float('inf') for node in self.adj_list}
        shortest_time[start] = 0
        visited = set()

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, travel_time in self.adj_list[current_node]:
                time = current_time + travel_time
                if time < shortest_time[neighbor]:
                    shortest_time[neighbor] = time
                    heapq.heappush(min_heap, (time, neighbor))

        return shortest_time

    # Display graph
    def display_graph(self):
        print("\nGraph connections (Location → Neighbors [Time in minutes]):")
        for node, edges in self.adj_list.items():
            print(f"{node} → {edges}")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    g = Graph()

    print("=== Pizza Delivery Route Planner ===")
    n = int(input("Enter number of roads (connections): "))

    print("\nEnter road details (Location1 Location2 TimeInMinutes):")
    for _ in range(n):
        u, v, t = input().split()
        g.add_edge(u, v, int(t))

    g.display_graph()

    start = input("\nEnter starting location (Pizza Shop): ")
    result = g.dijkstra(start)

    print("\n=== Minimum Time to Deliver Pizza from", start, "===")
    for location, time in result.items():
        print(f"To {location}: {time} minutes")

    # Find maximum time (i.e., last delivery)
    max_time = max(result.values())
    farthest = [loc for loc, t in result.items() if t == max_time]

    print("\nFarthest delivery location(s):", ", ".join(farthest))
    print("Total minimum time to deliver to all customers:", max_time, "minutes")
