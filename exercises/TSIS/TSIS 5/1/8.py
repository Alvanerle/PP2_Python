f = open('input.txt', 'r')
l = f.readlines()
s = ''

for x in l:
    s += x

l = s.split()
mx = 0
ans = ''
for x in l:
    if len(x) > mx:
        mx = len(x)
        ans = x
print(x)