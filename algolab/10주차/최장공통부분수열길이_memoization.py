def lcs_length_memo(x, y, m, n, memo):
    # 이미 계산된 경우 메모이제이션 배열에서 값 반환
    if memo[m][n] is not None:
        return memo[m][n]
    
    # 기본 조건: 하나의 문자열의 길이가 0이면 LCS 길이도 0
    if m == 0 or n == 0:
        memo[m][n] = 0
    elif x[m - 1] == y[n - 1]:  # 마지막 문자가 같을 경우
        memo[m][n] = 1 + lcs_length_memo(x, y, m - 1, n - 1, memo)
    else:  # 마지막 문자가 다를 경우
        memo[m][n] = max(lcs_length_memo(x, y, m - 1, n, memo), lcs_length_memo(x, y, m, n - 1, memo))
    
    return memo[m][n]

# 입력 받기
t = int(input())
for _ in range(t):
    x, y = input().split()
    m, n = len(x), len(y)
    # 메모이제이션 배열 초기화
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    # LCS 길이 계산 및 출력
    print(lcs_length_memo(x, y, m, n, memo))
