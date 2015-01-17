class Parent():

  """Docstring for Parent. """

  def __init__(self):
    """TODO: to be defined1. """
    print('Roberts')

  def print_last_name(self):
    print('Roberts')

class Child(Parent):

  """Docstring for Child. """

  def __init__(self):
    """TODO: to be defined1. """
    Parent.__init__(self)

  def print_first_name(self):
    print('Bucky')

  def print_last_name(self):
    print('Snitzelberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()
