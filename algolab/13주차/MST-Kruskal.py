class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges):
    uf = UnionFind(n + 1)
    mst_weight = 0
    edges_used = 0

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            edges_used += 1
            if edges_used == n - 1:
                break

    return mst_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])  # Number of test cases
    idx = 1
    results = []

    for _ in range(t):
        n = int(data[idx])  # Number of nodes
        idx += 1
        edges = []

        for _ in range(n):
            line = list(map(int, data[idx].split()))
            idx += 1
            node = line[0]
            m = line[1]
            connections = line[2:]

            for i in range(m):
                neighbor = connections[2 * i]
                weight = connections[2 * i + 1]
                if node < neighbor:  # Avoid duplicate edges
                    edges.append((node, neighbor, weight))

        # Compute MST weight
        result = kruskal(n, edges)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
