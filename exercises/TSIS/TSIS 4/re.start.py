import re 

s = input()
k = input()

pattern = re.compile(k)
matches = pattern.finditer(s)

for match in matches:
    print(match)
