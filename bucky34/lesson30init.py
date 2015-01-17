class Tuna():

    """this is my first __init__ in bucky's tutorial"""

    def __init__(self):
	"""TODO: practice using __init__ """
	print('bljkrekjrlekjr')


    def swim(self):
	print('I am swinning')


flipper = Tuna()
flipper.swim()

class Enemy():

    """Docstring for Enemy. """

    def __init__(self, x):
	"""TODO: to be defined1.

	:x: TODO

	"""

	self.energy = x


    def get_energy(self):
	print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)


jason.get_energy()
sandy.get_energy()
