# SyntaxError
# print 'hello world'
# This will make a synctax error because we forgot to enclose the
# string with parenthesis


# Name Error
# print(age)
# This displauy an error because the name age is not defined
# And we are trying to print it 

# IndexError
# Numbers = [1,5,6,7,8]
# numbers[5]
# This type of error is raise by python because the list has only indexes from 0 - 4
# So we are out of range


# ModuleNotFoundError
# import maths
# This occur when you try calling a module is not recognise by python
# Either wrong module name, module not install
# Like in the above we called wrong module name we import maths instead of math


# AttributeError
# import math
# math.PI
# This normally ocurs when you make a mistake in calling the attribute name or the attribute not associated with the module
# Like in the above we called math.PI instead of math.pio which is wronh attribute name


# KeyError
#  users = {'name':'Asab', 'age':250, 'country':'Finland'}
# users['county]
# This error occur when you make a key name mistake
# from our users dictionary we have country not county
# this type of error is called KeyError

# TypeError
# 4 + '3'
# TypeError is raised because we cannot add a number to a string


# ImportError 
# from math import power
# this error is raise when you try import a function that does not exist in module 
# There is no function called power in the math module, it goes with a different name: pow.

# ValueError
# int(12a)
# In this case we cannot change the given string to a number, because of the 'a' letter in it


# ZeroDivisionError
# 1/0
# we cant not divide a number by zero