from itertools import permutations

# 가중치를 계산하는 함수
def calculate_weight(s):
    weight = 0
    for i, char in enumerate(s):
        # 가중치 계산: (-1)^i * (ord(char) - ord('a'))
        weight += (-1)**i * (ord(char) - ord('a'))
    return weight

# 메인 함수
def stringPermutation(s):
    # 모든 순열을 생성
    perm = permutations(s)
    
    # 가중치가 양수인 순열의 개수를 카운트
    positive_count = 0
    for p in perm:
        if calculate_weight(p) > 0:
            positive_count += 1
    return positive_count

num = int(input())
for i in range(num):
  word = input()
  print(stringPermutation(word))