from collections import defaultdict

# Recursive DFS로 Connected Components 계산
def dfs(node, visited, graph, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, component)

# Connected Components 계산 함수
def connected_components(graph, n):
    visited = [False] * (n + 1)
    components = []
    
    for node in range(1, n + 1):
        if not visited[node]:
            component = []
            dfs(node, visited, graph, component)
            components.append(component)
    
    return components

# 입력 처리 및 출력
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])  # 테스트 케이스 수
    results = []
    index = 1
    for _ in range(t):
        n = int(data[index])  # 노드 수
        index += 1
        graph = defaultdict(list)
        for _ in range(n):
            line = list(map(int, data[index].split()))
            index += 1
            node, m, *neighbors = line
            graph[node].extend(neighbors)

        components = connected_components(graph, n)
        component_sizes = sorted(len(c) for c in components)
        results.append((len(components), component_sizes))

    for count, sizes in results:
        print(count, *sizes)

if __name__ == "__main__":
    main()
