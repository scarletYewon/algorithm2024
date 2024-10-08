import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    half = power(x, y // 2) % 1000
    if y % 2 == 0:
        return half% 1000 * half % 1000
    else:
        return x% 1000 * half% 1000 * half % 1000
    
num = int(input())
for i in range(num):
  a, n = map(int,input().split())
  print(str(power(a,n)% 1000)[-3:])