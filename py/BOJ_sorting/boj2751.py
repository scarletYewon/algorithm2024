import sys

input = sys.stdin.readline
n = int(input())
nList = []

for i in range(n):
  num = int(input())
  nList.append(num)

nList.sort()

for i in range(n):
  print(nList[i])