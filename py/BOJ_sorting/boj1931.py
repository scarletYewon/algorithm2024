n = int(input())
nList = []

for i in range(n):
  start, end = map(int, input().split())
  nList.append([start, end])

nList.sort(key=lambda x: (x[1], x[0]))

endPoint = 0
ans = 0

for s, e in nList:
  if s >= endPoint:
    endPoint = e
    ans +=1

print(ans)