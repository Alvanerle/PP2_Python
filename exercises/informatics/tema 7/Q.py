a = []
x = 1
sum = 0
while True:
    x = int(input())
    a.append(x)
    if a[len(a) - 1] == 0 and a[len(a) - 2] == 0:
        break
    sum += x
print(sum)