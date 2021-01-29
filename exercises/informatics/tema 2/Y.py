a = int(input())
b = int(input())

c = max(a, b)
d = min(a, b)

if c % d == 0:
    print(1)
else:
    print(0)
