x = -4
foods = ["bacon", "ham", "tuna", "sausages", "beef"]
TRUE = True
FALSE = False
# abs()
print( "abs(x):" , abs(x) )

# all()
# Return True if all elements of the iterable are true (or if the iterable is empty). 
# Equivalent to:
def all(iterable):
	for element in iterable:
		if not element:
			return False
		return True
print( "all(foods):" , all(foods) )

# any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False. 
# Equivalent to:
def any(iterable):
	for element in iterable:
		if element:
			return True
		return False
print( "any(foods):" , any(foods) )

# basestring()
# This abstract type is the superclass for str and unicode. 
# It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode. 
# isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).
# I dont' knnow how to test this?:basestring(foods)

# bin(x)
# Convert an integer number to a binary string. The result is a valid Python expression. 
# If x is not a Python int object, it has to define an __index__() method that returns an integer.
print( "bin(x):" , bin(x) )

# class bool([x])
# Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. 
# If x is false or omitted, this returns False; otherwise it returns True
# bool is also a class, which is a subclass of int
# Class bool cannot be subclassed further
# Its only instances are False and True.
print( "bool(TRUE):" , bool(TRUE) , "bool(FALSE):" , bool(FALSE) )
