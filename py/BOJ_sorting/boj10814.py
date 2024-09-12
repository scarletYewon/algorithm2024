n = int(input())
ageNameList = []

for i in range(n):
  age, name = map(str, input().split())
  ageNameList.append((int(age), name))

ageNameList.sort(key = lambda x : x[0])

for i in ageNameList:
  print(i[0], i[1])