# Hoare Partition 기반 퀵소트
def quicksort_hoare(arr, low, high, result):
    if low >= high:
        return
    p = partition_hoare(arr, low, high, result)
    quicksort_hoare(arr, low, p, result)
    quicksort_hoare(arr, p + 1, high, result)

def partition_hoare(arr, low, high, result):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            result['comparisons_hoare'] += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            result['comparisons_hoare'] += 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        result['swaps_hoare'] += 1

# Lomuto Partition 기반 퀵소트
def quicksort_lomuto(arr, low, high, result):
    if low >= high:
        return
    p = partition_lomuto(arr, low, high, result)
    quicksort_lomuto(arr, low, p - 1, result)
    quicksort_lomuto(arr, p + 1, high, result)

def partition_lomuto(arr, low, high, result):
    pivot = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        result['comparisons_lomuto'] += 1
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
            result['swaps_lomuto'] += 1
    arr[low], arr[j] = arr[j], arr[low]
    result['swaps_lomuto'] += 1
    return j

# 테스트 데이터 입력 및 처리
def process_test_case(test_case):
    result = {
        'swaps_hoare': 0,
        'comparisons_hoare': 0,
        'swaps_lomuto': 0,
        'comparisons_lomuto': 0
    }

    n = test_case[0]
    arr1 = test_case[1:]  # Hoare용 배열 복사
    arr2 = arr1[:]  # Lomuto용 배열 복사

    quicksort_hoare(arr1, 0, n - 1, result)
    quicksort_lomuto(arr2, 0, n - 1, result)

    return result

# 테스트 데이터 실행
t = int(input())  # 테스트 케이스 수 입력
for _ in range(t):
    test_case = list(map(int, input().split()))
    result = process_test_case(test_case)
    print(result['swaps_hoare'], result['swaps_lomuto'], result['comparisons_hoare'], result['comparisons_lomuto'])
