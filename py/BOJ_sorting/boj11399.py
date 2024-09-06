import sys

input = sys.stdin.readline

n = int(input())

times = list(map(int, input().split()))
times.sort()

times_sum = []
cnt = 0

for i in range(n):
  plus = cnt + times[i]
  cnt = plus
  times_sum.append(cnt)

print(sum(times_sum))

