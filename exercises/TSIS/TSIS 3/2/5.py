n = int(input())

d = {}

for i in range(n):
    s1, s2 = [i for i in input().split()]
    d[s1] = s2

s = input()

for key, value in d.items():
    if key == s:
        print(value)
        exit()
    if value == s:
        print(key)
        exit()

        