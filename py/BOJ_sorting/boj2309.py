ageList = []

for i in range(9):
  age = int(input())
  ageList.append(age)

ageList.sort()

ageSum = sum(ageList)

for i in range(9):
  for j in range(i+1, 9):
    if ageSum - ageList[i] - ageList[j] == 100:
      for k in range(9):
        if i == k or j==k:
          pass
        else:
          print(ageList[k])
      exit()