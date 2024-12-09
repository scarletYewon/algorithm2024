import heapq
from collections import defaultdict

def corrected_dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    parent = [-1] * (n + 1)  # To track the shortest path tree

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            if dist[neighbor] > current_dist + weight:
                dist[neighbor] = current_dist + weight
                parent[neighbor] = current_node
                heapq.heappush(pq, (dist[neighbor], neighbor))

    # Compute the weight of the shortest path tree
    total_weight = 0
    for node in range(1, n + 1):
        if parent[node] != -1:
            for neighbor, weight in graph[parent[node]]:
                if neighbor == node:
                    total_weight += weight
                    break

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

        for i in range(1, n + 1):
            line = list(map(int, data[idx].split()))
            idx += 1
            node = line[0]
            m = line[1]
            edges = line[2:]

            for j in range(m):
                neighbor = edges[j * 2]
                weight = edges[j * 2 + 1]
                graph[node].append((neighbor, weight))

        # Compute the shortest path tree weight starting from node 1
        result = corrected_dijkstra(n, graph, 1)
        results.append(result)

    # Output results
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
