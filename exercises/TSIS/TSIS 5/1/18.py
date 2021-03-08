f = open('test.txt', 'r')
l = f.readlines()
words = ''
for x in l:
    words += x
words = words.split()
print(len(words))
