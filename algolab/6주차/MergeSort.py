# def merge_sort(arr):
#     if len(arr) > 1:
#         # 중간 지점을 찾음
#         mid = len(arr) // 2
        
#         # 배열을 두 부분으로 나눔
#         left_half = arr[:mid]
#         right_half = arr[mid:]
        
#         # 좌우 부분을 재귀적으로 정렬하면서 비교 연산 횟수를 누적
#         cnt = merge_sort(left_half)
#         cnt += merge_sort(right_half)
        
#         i = j = k = 0
        
#         # 좌우 부분을 병합하여 정렬
#         while i < len(left_half) and j < len(right_half):
#             cnt += 1  # 비교 연산이 실행될 때마다 카운트 증가
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
        
#         # 남은 요소 병합
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
        
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     else:
#         cnt = 0  # 배열이 1개 이하일 경우 비교 연산이 없으므로 0을 반환

#     return cnt
    

# n = int(input())
# for i in range(n):
#     data = list(map(int, input().split()))
#     arr = data[1:]  # 첫 번째 값은 배열의 길이, 실제로 정렬할 배열은 그 뒤에 있음
#     print(merge_sort(arr))

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


