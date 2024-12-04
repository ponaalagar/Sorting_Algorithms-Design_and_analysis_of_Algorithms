# It is a graph sorting technique for Directed Acyclic Graphs (DAGs)

from collections import defaultdict, deque

def topologicalSort(vertices: int, edges: list) -> list:
    # Create adjacency list and in-degree array
    adj = defaultdict(list)
    in_degree = [0] * vertices

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # Find all vertices with 0 in-degree
    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != vertices:
        return "Graph is not a DAG (contains cycles)."
    return topo_order


# Example usage
vertices = int(input("Enter the number of vertices: "))
edges_count = int(input("Enter the number of edges: "))
print("Enter the edges (u v):")
edges = [tuple(map(int, input().split())) for _ in range(edges_count)]

sorted_order = topologicalSort(vertices, edges)
print("Topological Order:", sorted_order)

# Input size: n (vertices), e (edges)
# Basic operation: in-degree reduction and vertex removal
# Time complexity: O(n + e)
