a = list(map(int, input().split()))
k = int(input())

if k >= 0:
    k %= len(a)
    for i in range(len(a) - k, len(a)):
        print(a[i], end = " ")
    for i in range(len(a) - k):
        print(a[i], end = " ")
else:
    k *= -1
    k %= len(a)
    for i in range(k, len(a)):
        print(a[i], end = " ")
    for i in range(k):
        print(a[i], end = " ")



