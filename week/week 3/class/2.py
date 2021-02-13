  
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    pass



x = Person('John', 'Dorian')
x.printname()

s1 = Student('Adam', 'Eva')
s1.printname()