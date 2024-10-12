def merge(arr, tmp, low, mid, high):
    i = low
    j = mid + 1
    k = low
    cnt = 0  # 비교 연산자 실행 횟수

    # 임시 배열에 복사
    for i in range(low, high + 1):
        tmp[i] = arr[i]

    i = low
    while i <= mid and j <= high:
        cnt += 1  # 비교 연산자가 실행될 때마다 증가
        if tmp[i] <= tmp[j]:
            arr[k] = tmp[i]
            i += 1
        else:
            arr[k] = tmp[j]
            j += 1
        k += 1

    # 남은 왼쪽 부분 복사
    while i <= mid:
        arr[k] = tmp[i]
        i += 1
        k += 1

    # 남은 오른쪽 부분 복사
    while j <= high:
        arr[k] = tmp[j]
        j += 1
        k += 1

    return cnt


def iterative_merge_sort(arr):
    n = len(arr)
    tmp = [0] * n  # 임시 배열 생성
    cnt = 0  # 비교 연산자 실행 횟수

    # 각 부분 배열의 크기를 1부터 시작하여 점차적으로 두 배씩 늘려가며 병합
    size = 1
    while size < n:
        low = 0
        while low < n - 1:
            mid = min(low + size - 1, n - 1)
            high = min(low + 2 * size - 1, n - 1)
            print(low,mid,high)
            # 병합
            if mid < high:
                cnt += merge(arr, tmp, low, mid, high)

            low += 2 * size

        # 부분 배열 크기를 두 배로 증가시킴
        size *= 2

    return cnt


t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    data = list(map(int, input().split()))  # 입력받은 테스트 케이스 데이터
    n = data[0]  # 정수의 개수
    arr = data[1:]  # 실제 정렬할 배열
    comparison_count = iterative_merge_sort(arr)  # Iterative Merge Sort 실행 및 비교 연산 횟수 계산
    print(comparison_count)  # 결과 출력