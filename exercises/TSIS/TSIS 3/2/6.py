def my_comp(a):
    return(-a[0], a[1])

words = []
# почему - то не работает ввод
line = "test"
while line:
    line = input()
    tmp = line.split()
    for i in tmp:
        words.append(i)

d = {}
for x in words:
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1
ans = list(tuple())
for x in d:
    ans.append((d[x], x))
ans.sort(key = my_comp)

for x in ans:
    print(x[1])