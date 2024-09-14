import sys

input = sys.stdin.readline
n = int(input())
points = []

for i in range(n):
  point = list(map(int, input().split()))
  points.append(point)

# points 정렬하기
points = sorted(points, key=lambda x: (x[0], x[1]))
  
for i in points:
  print(i[0],i[1])