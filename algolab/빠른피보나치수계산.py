import sys
input = sys.stdin.readline

def mMul(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def mPow(M, power, mod):
    # 기본 행렬 (항등 행렬)
    rst = [[1, 0], [0, 1]]
    base = M
    while power:
      if power % 2 == 1:
        rst = mMul(rst, base, mod)
      base = mMul(base, base, mod)
      power //= 2
    return rst

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # 초기 피보나치 행렬 [[1, 1], [1, 0]]
  f = [[1, 1], [1, 0]]
  # 행렬 거듭제곱을 사용해 F^(n-1) 계산
  rst = mPow(f, n - 1, 1000)
  # F(n)의 마지막 세 자리는 행렬의 [0][0] 요소에 있음
  return rst[0][0]

num = int(input())
for i in range(num):
  n = int(input())
  ans = str(fibo(n))
  if len(ans)>3:
    print(ans[-3:])
  else:
    print(ans)