# Day 2: 30 Days of python programming
import keyword
first_Name = "Mubarak"
last_Name = "Abdullateef"

full_Name = "Abdullateef Mubarak"
country = "Nigeria"
city = "Abuja"
age = 21
year = 2023
is_Married = False
is_True = True
is_Light_On = True

hobbie, pet_Name, fav_Sport, age = "Reading", "Khalil", "Basketball", 5


print(type(first_Name))

print(type(last_Name))

print(type(full_Name))

print(type(country))

print(type(city))


print(type(age))
print(type(year))

print(type(is_Married))

print(type(is_True))

print("length of user firstName is: ", len(first_Name))

print(" firstName and LastName length comparison : ",
      len(first_Name) == len(last_Name))


num_one = 5
num_two = 4


total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two
division = num_two / num_one
remainder = num_one % num_two
exp = num_one ** num_two

floor_division = num_one // num_two
area_of_circle = (3.1415 * 30 ** 2)
circum_of_circle = (2 * 3.1415 * 30)

radius = input("Enter circle radius: ")
print("Area of circle from the radius entered is: ", (3.1415 * int(radius)**2))


first_Name = input("Enter First name: ")
print("first name is: ", first_Name)
last_Name = input("Enter Last Name : ")
print("Last name is: ", last_Name)

country = input("Enter your country : ")
print("Country is: ", country)

age = input("Enter your age: ")
print("Age  is: ", age)


help("keywords")
