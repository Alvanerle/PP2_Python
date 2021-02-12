a = []
x = 1
while x != 0:
    x = int(input())
    a.append(x)


for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        x += 1
print(x)