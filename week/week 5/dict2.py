car1 = {
    'name' : 'gtr',
    'year' : 1994,
    'model' : 'random'
}
car2 = {
    'name' : 'gtr',
    'year' : 2003,
    'model' : 'random'
}

for i1, i2 in zip(car1.items(), car2.items()):
    print(i1, i2)
    if i1 == i2:
        print('same')
    else:
        print('not same')