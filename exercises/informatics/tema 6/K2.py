s = input()

ind1 = s.find('h')
ind2 = s.rfind('h')

s = s.replace('h', 'H')

for i in range(len(s)):
    if i == ind1 or i == ind2:
        print('h', end = "")
    else:
        print(s[i], end = "")