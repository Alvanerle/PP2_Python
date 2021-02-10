s = input()

cnt = 0
ind = 0
for i in range(len(s)):
    if s[i] == 'f':
        cnt += 1
    if s[i] == 'f' and cnt == 2:
        ind = i

if cnt == 1:
    print(-1)
elif cnt == 0:
    print(-2)
else:
    print(ind)