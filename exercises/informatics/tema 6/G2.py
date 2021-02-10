s = input()

ind1 = s.index('h')
ind2 = s.rindex('h')

ans = s[:ind1]
tmp = s[ind1:ind2 + 1]
ans += tmp[::-1]
ans += s[ind2 + 1:]

print(ans)