Tarjan's algorithm is a graph algorithm used to find articulation points (or cut vertices) in an undirected graph. Articulation points are vertices whose removal increases the number of connected components in the graph.

Here's how Tarjan's algorithm works:

1. Perform a depth-first search (DFS) traversal of the graph, keeping track of the depth of each node and the lowest depth reachable from each node.
2. During the DFS traversal, mark nodes as visited and assign them a depth.
3. For each node, check if any of its adjacent nodes can reach a node with lower depth than the current node. If so, update the lowest reachable depth of the current node.
4. If the lowest reachable depth of any adjacent node is greater than or equal to the depth of the current node, then the current node is an articulation point.

Here's a Python implementation of Tarjan's algorithm:

```python
class Graph:
    def __init__(self, V):
        self.V = V  # Number of vertices
        self.adj = [[] for _ in range(V)]  # Adjacency list
        self.time = 0  # Time for DFS traversal
        self.articulation_points = set()  # Set to store articulation points

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def tarjan_dfs(self, u, parent, visited, low, disc):
        children = 0  # Count of children in DFS tree

        # Mark current node as visited and initialize discovery time and low value
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.adj[u]:
            # If v is not visited yet, then make it a child of u in DFS tree and recur for it
            if not visited[v]:
                children += 1
                self.tarjan_dfs(v, u, visited, low, disc)

                # Check if the subtree rooted with v has a connection to one of the ancestors of u
                low[u] = min(low[u], low[v])

                # u is an articulation point if one of the following two conditions is true:
                # 1. u is root of DFS tree and has two or more children
                # 2. If u is not the root and low value of one of its child is more than discovery value of u
                if parent == -1 and children > 1:
                    self.articulation_points.add(u)
                if parent != -1 and low[v] >= disc[u]:
                    self.articulation_points.add(u)

            # Update low value of u for parent function calls
            elif v != parent:
                low[u] = min(low[u], disc[v])

    def find_articulation_points(self):
        visited = [False] * self.V
        disc = [float("inf")] * self.V
        low = [float("inf")] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.tarjan_dfs(i, -1, visited, low, disc)

        return self.articulation_points

# Example usage:
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Articulation points in the graph:")
print(g.find_articulation_points())
```

This code defines a `Graph` class with methods to add edges and find articulation points using Tarjan's algorithm. The `find_articulation_points` method returns a set containing all the articulation points in the graph. You can create a graph object, add edges to it, and then call the `find_articulation_points` method to get the articulation points.