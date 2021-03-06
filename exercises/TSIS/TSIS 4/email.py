import re

pattern = r'\<[a-zA-Z]{1}[0-9-a-zA-Z._-]*\@[a-zA-Z]+\.[a-zA-Z]{1,3}\>'
ans = []

n = int(input())
for i in range(n):
    s = input()
    if re.search(pattern, s):
        ans.append(s)
print(*ans, sep = '\n')
