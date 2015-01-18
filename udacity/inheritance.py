class Parent():
    def __init__ (self, lastName, eyeColor):
	print("Parent constructor called")
	self.lastName = lastName
	self.eyeColor = eyeColor
    def showInfo(self):
	print("Last Name - " + self.lastName)
	print("Eye Color - " + self.eyeColor)

class Child(Parent):
    def __init__(self, lastName, eyeColor, toys):
	print("Child constructor called")
	Parent.__init__ (self, lastName, eyeColor)
	self.toys = toys
    def showInfo(self):
	print("Last Name - " + self.lastName)
	print("Eye Color - " + self.eyeColor)
	print("Number of toys - " + str(self.toys))

billyCyrus = Parent("Cyrus", "blue")
print(billyCyrus.lastName)

mileyCyrus = Child("Cyrus", "blue", 5)
print(mileyCyrus.lastName)
print(mileyCyrus.toys)

billyCyrus.showInfo()

mileyCyrus.showInfo()
