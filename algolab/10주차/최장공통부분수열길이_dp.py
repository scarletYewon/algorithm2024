def lcs_length_and_sequence(x, y):
    m, n = len(x), len(y)
    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # 문자가 같을 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다를 경우
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이
    lcs_length = dp[m][n]

    # LCS 문자열 추적
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:  # 문자가 같을 경우
            lcs_sequence.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # 위쪽 값이 더 크다면 위쪽으로 이동
            i -= 1
        else:  # 왼쪽 값이 더 크다면 왼쪽으로 이동
            j -= 1

    # 역순으로 추가된 LCS 문자열을 뒤집어서 올바른 순서로 만들기
    lcs_sequence.reverse()
    
    return lcs_length, ''.join(lcs_sequence)

# 입력 받기
t = int(input())
for _ in range(t):
    x, y = input().split()
    lcs_length, lcs_sequence = lcs_length_and_sequence(x, y)
    # 결과 출력
    if lcs_length > 0:
        print(lcs_length, lcs_sequence)
    else:
        print(lcs_length)
