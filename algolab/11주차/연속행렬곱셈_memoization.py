import sys

def matrix_chain_multiplication(dims, i, j, memo):
    # 기저 사례: 하나의 행렬만 남은 경우
    if i == j:
        return 0
    
    # 메모이제이션 확인
    if memo[i][j] != -1:
        return memo[i][j]

    # 최소 비용 초기화
    min_cost = sys.maxsize

    # 모든 분할 위치에 대해 최소 비용 계산
    for k in range(i, j):
        cost = (matrix_chain_multiplication(dims, i, k, memo) +
                matrix_chain_multiplication(dims, k + 1, j, memo) +
                dims[i - 1] * dims[k] * dims[j])

        # 최소 비용 갱신
        if cost < min_cost:
            min_cost = cost

    # 계산 결과를 메모이제이션 테이블에 저장
    memo[i][j] = min_cost
    return min_cost

# 입력 처리
t = int(input())
results = []

for _ in range(t):
    n = int(input())
    dims = list(map(int, input().split()))
    # 메모이제이션 테이블 초기화
    memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    # 최소 비용 계산
    result = matrix_chain_multiplication(dims, 1, n, memo)
    results.append(result)

# 결과 출력
for res in results:
    print(res)
