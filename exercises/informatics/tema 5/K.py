import math

a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - (4 * a * c)
if a == 0:
    if b != 0:
        print(-c / b)
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    d = math.sqrt(d)
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    print(min(x1, x1), end = " ")
    print(max(x1, x2))