import threading

class BuckysMessenger(threading.Thread):

    """Docstring for BuckysMessenger. """

#    def __init__(self):
#	"""TODO: to be defined1. """
#	#threading.T.__init__(self)

    def run(self):
	for _ in range(10):
	    print(threading.currentThread().getName())

x = BuckysMessenger(name='send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()
	
