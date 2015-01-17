class MyClass():

    """Docstring for MyClass. """

    def __init__(self):
	"""TODO: to be defined1. """
	print("something")	

    life =3
    def attack(self):
	print("ouch")
	self.life -=1

    def checkLife(self):
	if self.life <=0:
	    print("I am dead")
	else:
	    print(str(self.life)+" life left")

	
myClass1 = MyClass()
myClass1.attack()
myClass1.checkLife()
    

#class Enemy():
#    life = 3
#
#    def attack(self):
#        print("ouch")
#	self.life -= 1
#
#	
#    def checkLife(self):
#	if self.life <=0:
#	    print("I am dead")
#	else:
#	    print(str(self.life)+" life left")
#
#
#
#enemy1 = Enemy()
#enemy2 = Enemy()
#enemy1.attack()
#enemy1.attack()
#enemy1.checkLife()
#enemy2.checkLife()
