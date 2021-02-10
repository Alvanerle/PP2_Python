class Dog:
    def __init__(self, name):
        self.name = name
    def woof(self):
        print("Woof!")
    def get_name(self):
        return self.name

d = Dog("REX")

d.woof()
print(d.get_name())