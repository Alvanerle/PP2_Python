import re

file = open("abc.txt", "r", encoding="utf-8")
text = file.read() 

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"

BIN = re.search(BINPattern, text).group("BIN")
NDS = re.search(NDSPattern, text).group("NDS")

print(BIN, NDS)

file.close()