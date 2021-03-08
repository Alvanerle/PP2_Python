f = open('input.txt', 'r')
l = f.readlines()
s = ''
for x in l:
    s += x

l = s.split()
frequency = {}
for x in l:
    if x not in frequency.keys():
        frequency[x] = 1
    else:
        frequency[x] += 1

for key, value in frequency.items():
    print(key + ': ' + str(value))