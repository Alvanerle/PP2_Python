import re 

s = input()
Pattern = r"()"

print(re.search(Pattern, s).group("first"))