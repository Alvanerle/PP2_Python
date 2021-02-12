a = []
x = 1
mx = 0
while x != 0:
    x = int(input())
    a.append(x)
    mx = max(x, mx)
print(a.count(mx))