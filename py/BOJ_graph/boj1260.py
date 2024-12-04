from collections import deque

# DFS 함수
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# BFS 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 그래프 입력 처리
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited_dfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print()

# BFS 실행
visited_bfs = [False] * (n + 1)
bfs(graph, v, visited_bfs)
