three = [x for x in range(100) if x % 3 == 0]
print(three)

two_and_three = [x for x in three if x % 2 == 0]
print(two_and_three)

how_many_threes = [1 for x in range(100) if x % 3 == 0]
print(how_many_threes)

l = [0 for x in range(100)]
print(l)