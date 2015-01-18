x = -4
foods = ["bacon", "ham", "tuna", "sausages", "beef"]
TRUE = True
FALSE = False
# abs()
print( "abs(x):") , abs(x)

# all()
# Return True if all elements of the iterable are true (or if the iterable is empty). 
# Equivalent to:
def all(iterable):
	for element in iterable:
		if not element:
			return False
		return True
print( "all(foods):") , all(foods)

# any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False. 
# Equivalent to:
def any(iterable):
	for element in iterable:
		if element:
			return True
		return False
print( "any(foods):") , any(foods)

# basestring()
# This abstract type is the superclass for str and unicode. 
# It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode. 
# isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).
# I dont' knnow how to test this?:basestring(foods)

# bin(x)
# Convert an integer number to a binary string. The result is a valid Python expression. 
# If x is not a Python int object, it has to define an __index__() method that returns an integer.
print( "bin(x):"), bin(x)

# class bool([x])
# Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. 
# If x is false or omitted, this returns False; otherwise it returns True
# bool is also a class, which is a subclass of int
# Class bool cannot be subclassed further
# Its only instances are False and True.
print( "bool(TRUE):") , bool(TRUE) 
print( "bool(FALSE):") , bool(FALSE) 

# class bytearray([source[, encoding[, errors]]])
# Return a new array of bytes.
# The bytearray class is a mutable sequence of integers in the range 0 <= x < 256.
# It has most of the usual methods of mutable sequences, described in Mutable Sequence Types, as well as most methods that the str type has, see String Methods.
# I have no idea why I'd want to use this!!!

# callable(object)
# Return True if the object argument appears callable, False if not.
# If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed.
# Note that classes are callable (calling a class returns a new instance); class instances are callable if they have a __call__() method.
# I have no idea why I'd want to use this!!!

# chr(i)
# Return a string of one character whose ASCII code is the integer i.
# For example, chr(97) returns the string 'a'.
# This is the inverse of ord().
# The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. 
# See also unichr().
print("chr(97):"), chr(97)
