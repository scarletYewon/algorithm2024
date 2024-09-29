def gcd(a,b):
  tmp=0
  n=0
  if(a<b):
    tmp = a
    a = b
    b = tmp
  while(b!=0):
    n=a%b
    a=b
    b=n
  return a

num = int(input())
for i in range(num):
  a, b = map(int, input().split())
  print(gcd(a,b))