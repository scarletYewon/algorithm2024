import heapq
from collections import defaultdict

def corrected_prim(n, graph):
    visited = [False] * (n + 1)
    pq = [(0, 1)]  # (weight, node), starting from node 1
    total_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight

        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))

    return total_weight

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
        graph = defaultdict(list)

        for _ in range(n):
            line = list(map(int, data[idx].split()))
            idx += 1
            node = line[0]
            m = line[1]
            edges = line[2:]

            for i in range(m):
                neighbor = edges[2 * i]
                weight = edges[2 * i + 1]
                graph[node].append((neighbor, weight))
                graph[neighbor].append((node, weight))  # Undirected graph

        # Compute MST weight
        result = corrected_prim(n, graph)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
