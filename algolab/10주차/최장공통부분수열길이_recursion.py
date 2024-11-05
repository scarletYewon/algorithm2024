def lcs_length(x, y, m, n):
    # 기본 조건: 하나의 문자열의 길이가 0이면 LCS 길이도 0
    if m == 0 or n == 0:
        return 0
    
    # 마지막 문자가 같으면, LCS 길이에 1을 추가하고 두 문자열의 마지막 문자를 제외한 부분을 재귀적으로 호출
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs_length(x, y, m - 1, n - 1)
    
    # 마지막 문자가 다르면, 각각의 경우에 대해 LCS를 계산하고 더 큰 값을 선택
    else:
        return max(lcs_length(x, y, m - 1, n), lcs_length(x, y, m, n - 1))

# 입력 받기
t = int(input())
for _ in range(t):
    # 각 테스트 케이스에서 두 문자열 입력
    x, y = input().split()
    m, n = len(x), len(y)
    # LCS 길이 계산 및 출력
    print(lcs_length(x, y, m, n))
