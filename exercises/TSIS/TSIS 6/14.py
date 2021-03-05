s = input()
s = s.lower()

m = {}
for x in s:
    if x != ' ':
        if x in m.keys():
            m[x] += 1
        else:
            m[x] = 1
if len(m) == 26:
    print('This string is pangram')
else:
    print('This string is not pangram')
