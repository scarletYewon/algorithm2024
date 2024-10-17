import sys
sys.setrecursionlimit(10000)

lomuto_comp_count = 0
hoare_comp_count = 0
lomuto_swap_count = 0
hoare_swap_count = 0

def swap_elements(a, b):
    return b, a

def lomuto_partition(a, low, high):
    global lomuto_comp_count, lomuto_swap_count
    pivot = a[low]
    j = low
    for i in range(low + 1, high + 1):
        lomuto_comp_count += 1
        if a[i] < pivot:
            j += 1
            lomuto_swap_count += 1
            a[i], a[j] = swap_elements(a[i], a[j])
    lomuto_swap_count += 1
    a[low], a[j] = swap_elements(a[low], a[j])
    return j

def hoare_partition(a, low, high):
    global hoare_comp_count, hoare_swap_count
    pivot = a[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            hoare_comp_count += 1
            i += 1
            if a[i] >= pivot:
                break
        while True:
            hoare_comp_count += 1
            j -= 1
            if a[j] <= pivot:
                break
        if i < j:
            hoare_swap_count += 1
            a[i], a[j] = swap_elements(a[i], a[j])
        else:
            return j

def quick_sort_lomuto(v, low, high):
    if low < high:
        pivotPos = lomuto_partition(v, low, high)
        quick_sort_lomuto(v, low, pivotPos - 1)
        quick_sort_lomuto(v, pivotPos + 1, high)

def quick_sort_hoare(v, low, high):
    if low < high:
        pivotPos = hoare_partition(v, low, high)
        quick_sort_hoare(v, low, pivotPos)
        quick_sort_hoare(v, pivotPos + 1, high)

def main():
    global lomuto_comp_count, lomuto_swap_count, hoare_comp_count, hoare_swap_count
    t = int(input())  
    for _ in range(t):
        lomuto_comp_count = 0
        lomuto_swap_count = 0
        hoare_comp_count = 0
        hoare_swap_count = 0

        input_data = list(map(int, input().split())) 
        count = input_data[0]  
        nums_lomuto = input_data[1:] 
        nums_hoare = nums_lomuto[:] 

        quick_sort_lomuto(nums_lomuto, 0, count - 1)
        quick_sort_hoare(nums_hoare, 0, count - 1)
        
        print(f"{hoare_swap_count} {lomuto_swap_count} {hoare_comp_count} {lomuto_comp_count}")

if __name__ == "__main__":
    main()
