class Person:
    def __init__(self, fname, lname):
        print('parent')
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self, fname, lname):
        print('child')
        Person.__init__(self, fname, lname)



s1 = Student('Adam', 'Eva')
s1.printname()