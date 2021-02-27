class Person:
    name = "John"
    country = "Norway"

setattr(Person, 'age', 40)

# The age property will now have the value: 40

x = getattr(Person, 'age')
print(x)

p = Person()
print(p.age)
