import re 

pattern = r".(#[0-9-a-fA-F]{6}|#[0-9-a-fA-F]{3})"

t = int(input())
for i in range(t):
    s = input()
    ans = re.findall(pattern, s)
    if ans:
        print(*ans, sep = "\n")