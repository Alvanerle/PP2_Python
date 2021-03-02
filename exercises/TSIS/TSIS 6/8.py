a = list(map(int, input().split()))

m = {}

for x in a:
    if x in m.keys():
        m[x] += 1
    else:
        m[x] = 1

for key, value in m.items():
    if value == 1:
        print(key, end = ' ')
