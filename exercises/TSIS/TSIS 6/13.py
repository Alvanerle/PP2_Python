a = []

n = int(input())

for i in range(n + 1):
    tmp = []
    for j in range(i):
        if j == 0:
            tmp.append(1)
        elif j == i - 1:
            tmp.append(1)
        else:
            tmp.append(a[i - 1][j - 1] + a[i - 1][j])
    a.append(tmp)
for i in range(1, n + 1):
    for j in range(i):
        print(a[i][j], end = ' ')
    print()