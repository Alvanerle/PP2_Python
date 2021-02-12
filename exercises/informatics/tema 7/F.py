x = float(input())
y = float(input())

days = 1
while x < y:
    x *= 1.1
    days += 1
print(days)