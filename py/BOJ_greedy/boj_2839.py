def sugar_delivery(N):
    bag_count = 0
    while N >= 0:
        if N % 5 == 0:  # 남은 설탕이 5로 나누어 떨어지면
            bag_count += N // 5  # 5kg 봉지로 채우기
            return bag_count
        N -= 3  # 5kg으로 나눌 수 없을 경우, 3kg 봉지 하나 사용
        bag_count += 1
    return -1  # 정확히 나누지 못하는 경우
n = int(input())
print(sugar_delivery(n))