import sys

input = sys.stdin.readline

n = int(input())
nArr = set(map(int, input().split()))

m = int(input())
mArr = list(map(int, input().split()))

for i in mArr:
  if i in nArr:
    print(1)
  else:
    print(0)