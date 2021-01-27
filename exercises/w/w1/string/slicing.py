b = "abcdefghijklmn"
print(b[2:5])
print(b[:10])
print(b[10:])

a = "asdasdasfwef"
a = a.upper()
print(a)
a = a.lower()
print(a)

c = "Hello, Horld!"
print(c.replace("H", "J"))

d = "Hello, World!"
print(d.split(",")) # returns ['Hello', ' World!']

name = input("Enter your name: ")
age = input("Enter your age: ")
txt = "My name is {}, and I am {}"
print(txt.format(name, age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


txt = "We are the so-called \"Vikings\" from the north."
print(txt)