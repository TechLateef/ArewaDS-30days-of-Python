
# Higher Order Functions

# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

#     A function can take one or more functions as parameters
#     A function can be returned as a result of another function
#     A function can be modified
#     A function can be assigned to a variable

# Python Closures

# Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.
#  Let us have a look at how closures work in Python. 
# In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

# def add_ten():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

# closure_result = add_ten()
# print(closure_result(5))  # 15
# print(closure_result(10))  # 20

# Python Decorators

# A decorator is a design pattern in Python that allows a user to add new functionality
# to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.

# Normal function
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON

# ## Let us implement the example above with a decorator

# '''This decorator function is a higher order function
# that takes a function as a parameter'''
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON


# Applying Multiple Decorators to a Single Function

# '''These decorator functions are higher order functions
# that take functions as parameters'''

# # First Decorator
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # Second decorator
# def split_string_decorator(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper

# @split_string_decorator
# @uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
# def greeting():
#     return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON

# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to teach.".format(
#         first_name, last_name, country))

# print_full_name("Asabeneh", "Yetayeh",'Finland')

# 💻 Exercises: Day 14

from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map Applies a function to each element in a collection (list, tuple, etc.) 
# and returns a new collection with the transformed elements.

# Filter  Selects elements from a collection based on a predicate function. 
# It only keeps elements that return True for the predicate.

# Reduce  Combines all elements in a collection into a single value using a binary function. 
# It iteratively applies the function to pairs of elements until a single value remains.


# Higher Order function is a function that takes other function as argument
#  returning a function as it result, or both


# Closure A function that remembers and has access to variables defined outside its scope, even when the function is executed in another context.
#  This is achieved by enclosing the function within another function that creates a nested scope.

#  Decorator A function that wraps another function and modifies its behavior without changing its original code.
#  This modification can happen before, after, or around the execution of the original function.

def for_loop(lst):
    for item in lst:
        print(item)

country = for_loop(countries)

print(country)


name = for_loop(names)
print(name)

number_lst = for_loop(numbers)

print(number_lst)


countries_in_uppercase = map(lambda x: x.upper(), countries)

print(list(countries_in_uppercase))

number_sql = map(lambda x: x**2, numbers)

print(list(number_sql))


name_in_uppercase = map(lambda x: x.upper(), names)

print(list(name_in_uppercase))

contains_land = filter(lambda x:  'land' in x, countries)

print(list(contains_land))

# Print countrie that as 6  character
as_six_char = filter(lambda x: len(x) == 6, countries)

print(list(as_six_char))

# Print countrie that as 6 and more character
as_more_six_char = filter(lambda x: len(x) >= 6, countries)

print(list(as_more_six_char))

# print countrie that start with E
start_with_E = filter(lambda x: x[0] == 'E', countries)
print(list(start_with_E))

chain_iteration = map(lambda x: x**2, numbers)

evens = filter(lambda x: x % 2  == 0, chain_iteration)

even_lst = list(evens)
print(even_lst)
sum = reduce(lambda x, y: x + y, even_lst )

print(sum)

def get_string_lists(lst):
    strings = filter(lambda x: type(x) == type(''), lst)
    return list(strings)


print(get_string_lists( [1, 2, 3, 4, 5, 6, 7, 8, "9", "10"]))

sum = reduce(lambda x, y: x + y, numbers )

print(sum)


def sentence(acc, country):
  if country == countries[-1]:
    return f"{acc} and {country} are north European countries"
  else:
    return f"{acc}, {country}"

final_sentence = reduce(sentence, countries)

print(final_sentence) 