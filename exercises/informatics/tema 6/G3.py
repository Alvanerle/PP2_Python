s = input()

ind1 = s.index('h')
ind2 = s.rindex('h')

for i in range(ind2):  
    print(s[i], end = '')
for i in range(ind1 + 1, len(s)):
    print(s[i], end = '')

