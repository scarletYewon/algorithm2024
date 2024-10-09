def stringReverse(str):
  if len(str) == 1:
    return str
  else:
    return stringReverse(str[1:]) + str[0]
  
num = int(input())
for i in range(num):
  word = input()
  print(stringReverse(word))