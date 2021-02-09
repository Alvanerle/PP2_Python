a = list(map(int, input().split()))
b = list(map(int, input().split()))

s1 = set()
s2 = set()

for x in a:
    s1.add(x)
for x in b:
    s2.add(x)

s = s1.intersection(s2)
print(len(s))