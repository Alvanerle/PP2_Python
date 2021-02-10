s = input()

if s.find('f') != -1:
    ind1 = s.index('f')
    ind2 = s.rindex('f')
    print(ind1)
    if ind1 != ind2:
        print(ind2)
    