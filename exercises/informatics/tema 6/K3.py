s = input()

ans = ''
for i in range(len(s) - 1):
    ans += s[i] + '*'
ans += s[len(s) - 1]

print(ans)