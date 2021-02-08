s = input()

cnt = 0
last = 0
for i in range(len(s)):
    if s[i] == " " and last != i - 1:
        cnt += 1    
    if s[i] == " ":
        last = i


print(cnt + 1)