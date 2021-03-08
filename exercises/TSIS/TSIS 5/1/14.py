f1 = open('abc.txt', 'r')
f2 = open('abs.txt', 'r')

# I assume that they contain equal amount of lines
l1 = f1.readlines()
l2 = f2.readlines()

f = open('abd.txt', 'w')
for i in range(len(l1)):
    f.write(l1[i] + l2[i])
f.close()
f = open('abd.txt', 'r')
print(f.read())