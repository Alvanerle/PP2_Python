f = open('input.txt', 'r')
l = f.readlines()

n = int(input())
m = len(l)
for i in range(m - n, m):
    print(l[i], end = '')