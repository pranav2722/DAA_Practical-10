def kruskal(vertices, edges):
    parent = list(range(vertices))

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        parent[find(u)] = find(v)

    edges.sort(key=lambda x: x[2])
    mst = []
    cost = 0

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            cost += w

    print("\nMinimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    if len(mst) == vertices - 1:
        print("Total Cost:", cost)
    else:
        print("Graph is disconnected. MST is not possible.")


vertices = int(input("Enter number of vertices: "))
n = int(input("Enter number of edges: "))

edges = []
print("Enter edges (source destination weight):")

for i in range(n):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

kruskal(vertices, edges)
