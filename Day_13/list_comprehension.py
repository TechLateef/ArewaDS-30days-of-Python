# List comprehension in Python is a compact way of creating a list from 
# a sequence. It is a short way to create a new list.
#  List comprehension is considerably faster than processing
#  a list using the for loop.

# syntax
# [i for i in iterable if expression]

# Example:1

# For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

# # One way
# language = 'Python'
# lst = list(language) # changing the string to list
# print(type(lst))     # list
# print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# # Second way: list comprehension
# lst = [i for i in language]
# print(type(lst)) # list
# print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Example:2

# List comprehension can be combined with if expression

# # Generating even numbers
# even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
# print(even_numbers) 

# Flattening a three dimensional array
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [ number for row in list_of_lists for number in row]
# print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Lambda Function

# Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. 
# Lambda function is similar to anonymous functions in JavaScript. 
# We need it when we want to write an anonymous function inside another function.


# Creating a Lambda Function

# To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. See the syntax and the example below.
# Lambda function does not use return but it explicitly returns the expression.

# syntax
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))

# Lambda Function Inside Another Function

# Using a lambda function inside another function.

# def power(x):
#     return lambda n : x ** n

# cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
# print(cube)          # 8
# two_power_of_five = power(2)(5) 
# print(two_power_of_five)  # 32

# 💻 Exercises: Day 13

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtering = [i for i in numbers if i <= 0]

print(filtering)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

one_dimention = [item for lists in list_of_lists for list in lists for item in list]

print(one_dimention)

numbers = [(i, 1 , i * 1 ,i * i, i**3, i**4, i**5) for i in range(11)]

print(numbers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_list = [list(country)[:1] + [country[0][:3]] + list(country)[1:] for countries_set in countries for country in countries_set]
print(countries_list)

country_lst = [list(country) for countries_set in countries for country in countries_set]

print(country_lst)

to_dic = lambda countries_lst: {'country': countries_lst[0], 'city':countries_lst[1]}

country_dic = [to_dic(country) for country in country_lst]

print(country_dic)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [f"{name[0]} {name[1]}" for sublist in names for name in sublist]

print(output)