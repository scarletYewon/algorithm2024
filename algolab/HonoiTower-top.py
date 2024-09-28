def hanoi_tower(rst,three,n, start, end) :
    if n == 1 :
        if end ==3:
          three.append(str(n))
          rst.append(str(n))
        elif start ==3:
          if len(three) == 1:
            rst.append("0")
            three.pop()
          else:
            three.pop()
            rst.append(str(three[-1]))
        return rst,three

    hanoi_tower(rst,three,n-1, start, 6-start-end) # 1단계
    if end ==3:
      three.append(str(n))
      rst.append(str(n))
    elif start ==3:
      if len(three) == 1:
        rst.append("0")
        three.pop()
      else:
        three.pop()
        rst.append(str(three[-1]))
    hanoi_tower(rst,three,n-1, 6-start-end, end) # 3단계
    return rst,three

n = int(input())
for i in range(n):
    a = int(input())
    rst = []
    three = []
    print(" ".join(hanoi_tower(rst,three,a, 1, 3)[0]))