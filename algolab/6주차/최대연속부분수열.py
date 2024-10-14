def max_crossing_sum(arr, left, mid, right):
    # 왼쪽 부분에서의 최대 합 계산
    left_sum = float('-inf')
    sum_left = 0
    for i in range(mid, left - 1, -1):
        sum_left += arr[i]
        if sum_left > left_sum:
            left_sum = sum_left

    # 오른쪽 부분에서의 최대 합 계산
    right_sum = float('-inf')
    sum_right = 0
    for i in range(mid + 1, right + 1):
        sum_right += arr[i]
        if sum_right > right_sum:
            right_sum = sum_right

    # 중간을 포함하는 최대 합 반환
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    # 배열이 하나의 원소만 있을 경우
    if left == right:
        return arr[left]

    # 배열의 중간을 계산
    mid = (left + right) // 2

    # 왼쪽, 오른쪽, 그리고 중간을 포함하는 최대합 계산
    left_sum = max_subarray_sum(arr, left, mid)
    right_sum = max_subarray_sum(arr, mid + 1, right)
    cross_sum = max_crossing_sum(arr, left, mid, right)

    # 세 부분 중에서 최대합을 반환
    return max(left_sum, right_sum, cross_sum)

def find_maximum_sum(arr):
    if all(x < 0 for x in arr):
        max_sum = 0
    else:
        max_sum = max_subarray_sum(arr, 0, len(arr) - 1)
    return max_sum

n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    rst = find_maximum_sum(arr[1:])
    print(rst)