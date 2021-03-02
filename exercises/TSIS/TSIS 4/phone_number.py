import re

t = int(input())

for i in range(t):
    s = input()
    pattern = r"^[789][0-9]{9}$"
    if re.search(pattern, s):
        print('YES')
    else:
        print('NO')