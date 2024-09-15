n = int(input())
points = []

for i in range(n):
  a,b = map(int, input().split())
  points.append([a,b])

points.sort(key = lambda x: (x[1], x[0]))

for i in points:
  print(i[0], i[1])
