s = input()

ind1 = s.index('h')
ind2 = s.rindex('h')

tmp = [s[x] for x in range(len(s)) if x < ind1 or x > ind2]

for i in range(len(tmp)):
    print(tmp[i], end = "")