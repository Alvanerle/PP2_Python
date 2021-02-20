import re

file = open("abc.txt", "r", encoding="utf-8")
text = file.read() 

# BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
# NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"

# BIN = re.search(BINPattern, text).group("BIN")
# NDS = re.search(NDSPattern, text).group("NDS")

itemPatternText = r"\n{1}(?P<name>.*)\n{1}(?P<count>.*)x(?P<cost>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)

for x in re.finditer(itemPattern, text):
    print(x.group('name') + '-' + x.group('count') + 'x' + x.group('cost') + '=' + x.group('total1'))

file.close()