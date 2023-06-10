import sys

# Graph class to represent the network topology
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    # Add an edge to the graph
    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    # Dijkstra's algorithm to find the shortest path
    def dijkstra(self, src, dest):
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0

        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        print("Shortest path from source to destination:")
        self.print_path(dist, dest)
        print("\nTotal cost:", dist[dest])

    # Find the vertex with the minimum distance value
    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = -1

        for v in range(self.vertices):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    # Print the shortest path from source to destination
    def print_path(self, dist, dest):
        if dist[dest] == sys.maxsize:
            print("No path found.")
            return

        path = []
        curr = dest
        while curr != -1:
            path.append(curr)
            curr = self.get_previous(dist, curr)

        print(" -> ".join(map(str, path[::-1])))

    # Get the previous node in the shortest path
    def get_previous(self, dist, curr):
        for v in range(self.vertices):
            if dist[v] + self.graph[v][curr] == dist[curr]:
                return v
        return -1


# Create a sample network topology
network = Graph(5)
network.add_edge(0, 1, 10)
network.add_edge(0, 3, 5)
network.add_edge(1, 2, 1)
network.add_edge(1, 3, 2)
network.add_edge(2, 4, 4)
network.add_edge(3, 1, 3)
network.add_edge(3, 2, 9)
network.add_edge(3, 4, 2)
network.add_edge(4, 0, 7)
network.add_edge(4, 2, 6)

# Find the shortest path using Dijkstra's algorithm
network.dijkstra(0, 4)
