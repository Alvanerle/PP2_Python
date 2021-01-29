n = int(input())

a = int(n / 1000)
b = int(n / 100 % 10)
c = int(n / 10 % 10)
d = int(n % 10)

if a == d and c == b:
    print(1)
else:
    print(-1)