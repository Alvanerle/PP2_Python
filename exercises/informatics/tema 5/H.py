p = int(input())
x = int(input())
y = int(input())

res = (p / 100) * (y + x * 100) + (y + x * 100)

print(str(int(res / 100)) + " " + str(int(res % 100)))
