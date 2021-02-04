p = int(input())
x = int(input())
y = int(input())
k = int(input())

res = 0
for i in range(k):
    res = (p / 100) * (y + x * 100) + (y + x * 100)
    x = int(res / 100)
    y = int(res) % 100

print(str(int(res / 100)) + " " + str(int(res % 100)))
