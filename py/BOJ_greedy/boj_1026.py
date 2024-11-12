def solve(n,a,b):
  a.sort()
  b.sort(reverse=True)
  rst = 0
  for i in range(n):
    num = a[i]*b[i]
    rst+=num
  return rst

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n,a,b))
