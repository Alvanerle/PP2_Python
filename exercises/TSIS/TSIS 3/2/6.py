lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    elif line == "0":
        break

d = {}
for x in lines:
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 0

t = tuple(d)

print(t)