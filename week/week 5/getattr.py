class Person:
    name = 'John'
    age = 36 
    country = 'Norway'

p = Person()
p2 = Person()

p2.name = 'Bob'

attr = input()
print(getattr(p2, attr, 'not found'))