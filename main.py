import re

print ("Hello, please, enter filename (example filename: text.txt):")

entry = str(input())

with open(entry) as file:
  Text = file.readlines()

print ("Required lines:")

for i in range(len(Text)):
  numbersTest1 = re.search('([^\d]|^)(?:(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)([^\d]|$)', Text[i], flags=re.MULTILINE)

  if numbersTest1 != None:
    print (Text[i])
