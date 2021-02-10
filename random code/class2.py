class Dog:
    def __init__(self, name, age = 12):
        self.name = name
        self.age = age
    def woof(self):
        print("Woof!")
    def get_inf(self):
        return self.name + " " + str(self.age)
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


d = Dog("REX", 8)

print(d.get_inf())
print(d.get_name(), d.get_age())
