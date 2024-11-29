from collections import defaultdict

def solve_word_math():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    
    # 알파벳 가중치 계산
    weight = defaultdict(int)
    for word in words:
        power = len(word) - 1
        for char in word:
            weight[char] += 10 ** power
            power -= 1
    
    # 가중치가 높은 순서대로 정렬
    sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)
    
    # 숫자 배정
    num = 9
    char_to_num = {}
    for char, _ in sorted_weights:
        char_to_num[char] = num
        num -= 1
    
    # 단어들의 값을 계산
    total = 0
    for word in words:
        value = 0
        for char in word:
            value = value * 10 + char_to_num[char]
        total += value
    
    print(total)

# 실행
solve_word_math()
