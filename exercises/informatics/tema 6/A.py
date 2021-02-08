s = input()

print(s[2])
print(s[len(s) - 2])
print(s[:5])
print(s[:len(s) - 2])
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end = "")
print()
for i in range(len(s)):
    if i % 2:
        print(s[i], end = "")
print()
s2 = ""
for i in range(len(s) - 1, -1, -1):
    print(s[i], end = "")
    s2 += s[i]
print()
for i in range(len(s2)):
    if i % 2 == 0:
        print(s2[i], end = "")
print()
print(len(s))

