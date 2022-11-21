import re

print ("Hello, please, enter filename (example filename: text.txt):")

entry = str(input())
#entry = "text.txt"

with open(entry) as file:
  Text = file.readlines()

print ("Required lines:")

for i in range(len(Text)):
  numbersTest = re.search(r'[0-1]{2,}', Text[i])
  numbersBinaryNotation = re.findall(r'[0-1]{2,}', Text[i])
  if numbersTest != None:
    for j in range(len(numbersBinaryNotation)):
      k = int(numbersBinaryNotation[j], 2)
      if k%3 == 0:
        print ( Text[i])
        break;
