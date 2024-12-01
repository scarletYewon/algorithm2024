def next_permutation(n, s):
    # 문자열을 리스트로 변환
    s = list(s)

    # 1. 뒤에서부터 첫 번째 감소하는 인덱스를 찾는다.
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    # 2. 만약 감소하는 인덱스가 없으면, 가장 첫 번째 순열로 돌아간다.
    if i == -1:
        return ''.join(sorted(s))

    # 3. 뒤에서부터 첫 번째 s[i]보다 큰 값을 찾는다.
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1

    # 4. 두 값을 교환한다.
    s[i], s[j] = s[j], s[i]

    # 5. i+1부터 끝까지를 오름차순으로 정렬한다.
    s = s[:i + 1] + sorted(s[i + 1:])
    
    return ''.join(s)

# 테스트 입력 받기
t = int(input())
results = []
for _ in range(t):
    n, s = input().split()
    n = int(n)
    results.append(next_permutation(n, s))

# 결과 출력
for result in results:
    print(result)
