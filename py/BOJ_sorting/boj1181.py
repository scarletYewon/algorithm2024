import sys

input = sys.stdin.readline

n = int(input())
words = []

for i in range(n):
  word = input().rstrip()
  words.append(word)

words = list(set(words))

words = sorted(words,key=lambda x: (len(x),x))

for i in words:
  print(i)