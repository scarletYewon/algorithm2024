def kadane(arr):
    n = len(arr)
    
    # 초기 값 설정
    max_sum = float('-inf')  # 최대 합
    current_sum = 0  # 현재 부분 배열의 합
    start = 0  # 현재 부분 배열의 시작점
    best_start = -1  # 최대 합을 갖는 구간의 시작점
    best_end = -1  # 최대 합을 갖는 구간의 끝점
    length_of_best = float('inf')  # 가장 짧은 구간의 길이를 저장
    
    for i in range(n):
        # 0이 시작되는 부분 배열은 제외
        if current_sum == 0 and arr[i] == 0:
            start = i + 1
            continue
        
        if current_sum == 0:
            start = i
        
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i
            length_of_best = best_end - best_start + 1
        elif current_sum == max_sum:
            current_length = i - start + 1
            if start < best_start or (start == best_start and current_length < length_of_best):
                best_start = start
                best_end = i
                length_of_best = current_length
        
        # 합이 음수이면 현재 부분 배열을 버리고 새로운 구간을 시작
        if current_sum < 0:
            current_sum = 0

    # 결과 출력
    if max_sum < 0:
        max_sum = 0
        best_start = -1
        best_end = -1
    return max_sum,best_start,best_end


n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    rst = kadane(arr[1:])
    print(rst[0],rst[1],rst[2])