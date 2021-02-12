x = int(input())
p = int(input())
y = int(input())

p /= 100
p += 1

days = 0

x *= 100
y *= 100
while x < y:
    x *= p 
    x = int(x)
    days += 1
print(days)