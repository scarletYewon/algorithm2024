import sys

def matrix_chain_multiplication(dims, i, j):
    # 기저 사례: 하나의 행렬만 남은 경우
    if i == j:
        return 0
    
    # 최소 비용을 큰 값으로 초기화
    min_cost = sys.maxsize

    # 모든 분할 위치에 대해 반복
    for k in range(i, j):
        # k 위치에서의 분할에 대한 재귀적 비용 계산
        cost = (matrix_chain_multiplication(dims, i, k) +
                matrix_chain_multiplication(dims, k + 1, j) +
                dims[i - 1] * dims[k] * dims[j])

        # 최소 비용 갱신
        if cost < min_cost:
            min_cost = cost

    return min_cost

# 입력 처리
t = int(input())
results = []

for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    dims = data[1:]
    # 전체 범위에 대해 최소 비용 계산
    result = matrix_chain_multiplication(dims, 1, n)
    results.append(result)

# 각 테스트 케이스의 결과 출력
for res in results:
    print(res)
