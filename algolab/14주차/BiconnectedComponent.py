from collections import defaultdict

# Biconnected Components 및 Articulation Points 탐색
def find_biconnected_components_and_articulation_points(graph, n):
    time = 0
    low = [0] * (n + 1)
    disc = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    ap = set()
    bcc_count = 0
    stack = []

    def dfs(u):
        nonlocal time, bcc_count
        children = 0
        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:  # v가 방문되지 않은 경우
                parent[v] = u
                children += 1
                stack.append((u, v))  # Edge를 스택에 저장
                dfs(v)

                # Subtree에서 역방향 간선을 통해 갈 수 있는 가장 높은 노드 탐색
                low[u] = min(low[u], low[v])

                # (u, v)가 BCC를 나누는 간선인지 체크
                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                    ap.add(u)
                    bcc_count += 1
                    while stack[-1] != (u, v):
                        stack.pop()
                    stack.pop()  # (u, v) 제거
            elif v != parent[u]:  # 역방향 간선
                low[u] = min(low[u], disc[v])
                if (u, v) not in stack and (v, u) not in stack:
                    stack.append((u, v))

    for i in range(1, n + 1):
        if disc[i] == -1:
            dfs(i)
            if stack:
                bcc_count += 1
                stack.clear()

    return bcc_count, sorted(ap)

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
        for i in range(1, n + 1):
            line = list(map(int, data[index].split()))
            index += 1
            node, m, *neighbors = line
            graph[node].extend(neighbors)

        bcc_count, ap = find_biconnected_components_and_articulation_points(graph, n)
        results.append((bcc_count, ap))

    for bcc_count, ap in results:
        print(bcc_count)
        if ap:
            print(len(ap), *ap)
        else:
            print(0)

if __name__ == "__main__":
    main()
