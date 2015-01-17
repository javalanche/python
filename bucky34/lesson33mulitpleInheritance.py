class Mario():

  """Docstring for Mario. """

  def move(self):
    """TODO: to be defined1. """
    print('I a moving!')

class Shroom():

  """Docstring for Shroom. """

  def eat_shroom(self):
    """TODO: to be defined1. """
    print("Now I am big!")
    
class BigMario(Mario, Shroom):

  """Docstring for BigMario. """
  pass

bm = BigMario()
bm.move()
bm.eat_shroom()

