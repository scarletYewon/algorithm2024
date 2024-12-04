def calculate_weights(pebbles):
    left = pebbles[0]  # 첫 번째 자갈을 왼쪽에
    right = pebbles[1]  # 두 번째 자갈을 오른쪽에

    # 3번 자갈부터 배치
    for i in range(2, len(pebbles)):
        if left == right:
            left += pebbles[i]
        elif left < right:
            left += pebbles[i]
        else:
            right += pebbles[i]

    # 최종적으로 양쪽 무게 차이를 구함
    diff = abs(left - right)

    # 필요한 추가 무게추 개수 계산
    weights = [100, 50, 20, 10, 5, 2, 1]
    count = 0
    for weight in weights:
        if diff == 0:
            break
        count += diff // weight
        diff %= weight

    return count

# 입력 처리
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    pebbles = list(map(int, input().split()))
    results.append(calculate_weights(pebbles))

# 결과 출력
for result in results:
    print(result)
