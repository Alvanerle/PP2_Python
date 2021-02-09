tmp = list(map(int, input().split()))
n = tmp[0]
m = tmp[1]

s1 = set()
s2 = set()
for i in range(n):
    s1.add(int(input()))
for i in range(m):
    s2.add(int(input()))

ans1 = s1.intersection(s2)

a = list(ans1)
a.sort()
print(len(a))
for x in a:
    print(x, end = " ")

ans2 = s1.difference(s2)
b = list(ans2)
b.sort()
print("\n" + str(len(b)))
for x in b:
    print(x, end = " ")

ans3 = s2.difference(s1)
c = list(ans3)
c.sort()
print("\n" + str(len(c)))
for x in c:
    print(x, end = " ")


