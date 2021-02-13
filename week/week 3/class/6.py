
class Person:
    def __init__(self, fname, lname):
        print('parent')
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self, fname, lname, year):
        print('child')
        super().__init__(fname, lname)
        self.year = year
    def printname(self):
        super().printname()
        print(self.year)




s1 = Student('Adam', 'Eva', 2018)
s1.printname()