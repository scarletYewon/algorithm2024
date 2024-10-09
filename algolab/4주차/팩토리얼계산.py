import sys
sys.setrecursionlimit(2000)

def factorial(a):
  if a == 0:
    return 1
  else:
    return a * factorial(a-1)

num = int(input())
for i in range(num):
  n = int(input())
  print(str(factorial(n)).replace('0','')[-3:])