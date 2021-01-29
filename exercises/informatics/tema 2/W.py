h = int(input())
a = int(input())
b = int(input())

tmp = 0
days = 0

while True:
    tmp += a
    days += 1
    if tmp >= h:
        print(days)
        exit(0)
    tmp -= b