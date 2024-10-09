def SelectionSort(n,arr):
  cnt1 =0 # 비교횟수
  cnt2 = 0 # 교환횟수
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      cnt1 += 1
      if arr[j] < arr[min_idx]:
          min_idx = j
    if min_idx != i:
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
      cnt2 += 1
  return [cnt1,cnt2]

num = int(input())
for i in range(num):
  data = list(map(int, input().split()))
  n = data[0] 
  arr = data[1:n+1]
  cnt1,cnt2 = SelectionSort(n,arr)
  print(cnt1,cnt2)