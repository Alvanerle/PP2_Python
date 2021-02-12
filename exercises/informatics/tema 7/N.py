a = []
x = 1
mx = 0
while x != 0:
    x = int(input())
    a.append(x)
    mx = max(x, mx)


mx2 = 0
for i in range(len(a)):
    if a[i] != mx:
        mx2 = max(mx2, a[i])
print(mx2)