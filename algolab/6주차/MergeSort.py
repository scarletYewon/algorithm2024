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


def merge_sort(arr, tmp, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2

        # 좌우 부분을 재귀적으로 정렬
        cnt += merge_sort(arr, tmp, low, mid)  # 왼쪽 부분 정렬
        cnt += merge_sort(arr, tmp, mid + 1, high)  # 오른쪽 부분 정렬

        # 좌우 부분 병합 및 비교 연산 횟수 카운트
        cnt += merge(arr, tmp, low, mid, high)

    return cnt


t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    data = list(map(int, input().split()))  # 입력받은 테스트 케이스 데이터
    n = data[0]  # 정수의 개수
    arr = data[1:]  # 실제 정렬할 배열
    tmp = [0] * n  # 임시 배열 생성
    comparison_count = merge_sort(arr, tmp, 0, n - 1)  # Merge Sort 실행 및 비교 연산 횟수 계산
    print(comparison_count)  # 결과 출력


