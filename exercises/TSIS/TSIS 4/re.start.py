import re 

s = input()
k = input()

pattern = re.compile(k)
find = pattern.search(s)

if not find:
    print('(-1, -1)')
else:
    while find:
        print("({}, {})".format(find.start(), find.end() - 1))
        find = pattern.search(s, find.start() + 1)