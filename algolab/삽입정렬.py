def InsertionSort(n,arr):
  cnt1 =0 # 비교횟수
  cnt2 = 0 # 교환횟수
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0:
      cnt1 += 1 
      if arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        cnt2 += 1 
      else:
        break
    arr[j + 1] = key
  return [cnt1,cnt2]

num = int(input())
for i in range(num):
  data = list(map(int, input().split()))
  n = data[0] 
  arr = data[1:n+1]
  cnt1,cnt2 = InsertionSort(n,arr)
  print(cnt1,cnt2)