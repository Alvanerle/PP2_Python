left_range = int(input())
right_range = int(input())

def f(x):
    if x >= left_range and x <= right_range:
        return True
    return False

x = int(input())

if f(x):
    print('{} is in the range ({}, {})'.format(x, left_range, right_range))