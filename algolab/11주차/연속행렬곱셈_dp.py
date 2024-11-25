import sys

def matrix_chain_order(dims):
    n = len(dims) - 1  # 행렬 개수
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    
    # 길이 2 이상인 부분 문제들에 대해 DP 테이블 채우기
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split

def print_optimal_parens(split, i, j):
    if i == j:
        return f"M{i+1}"
    else:
        return f"({print_optimal_parens(split, i, split[i][j])}{print_optimal_parens(split, split[i][j] + 1, j)})"

# 입력 처리
t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    dims = list(map(int, input().strip().split()))
    
    # DP 및 split 테이블 생성
    dp, split = matrix_chain_order(dims)
    
    # 최적의 괄호 묶음 방식과 최소 곱셈 횟수
    optimal_parens = print_optimal_parens(split, 0, n - 1)
    min_multiplications = dp[0][n - 1]
    
    results.append((optimal_parens, min_multiplications))

# 결과 출력
for res in results:
    print(res[0])
    print(res[1])