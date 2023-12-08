# # Exercise-1

# age = int(input("Enter your age: "))

# if age >= 18:
#     print('You are older enough to learn to drive')

# else:
#     print(f"You need {18 - age} more years to learn to drive")


# my_age = 12

# your_age = int(input("Enter your age: "))

# if your_age > my_age:
#     print(f"You are {your_age - my_age} older than me.")

# elif my_age == your_age:
#     print("we are of same age")
# else:
#     print(f"I am {my_age - your_age} older than you ")


# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))

# if a > b:
#     print(f"{a} is greater than {b} ")
# elif b > a:
#     print(f"{b} is greater than {a} ")
# else:
#     print(f"{a} is equal to {b} ")


# def calculate_grade(score):
#     """
#     This function takes a score and returns the corresponding grade.

#     Args:
#         score: An integer representing the student's score.

#     Returns:
#         A string representing the student's grade.
#     """
#     if score >= 80 and score <= 100:
#         return "A"
#     elif score >= 70 and score <= 89:
#         return "B"
#     elif score >= 60 and score <= 69:
#         return "C"
#     elif score >= 50 and score <= 59:
#         return "D"
#     else:
#         return "F"


# # Example usage
# scores = [85, 72, 68, 55, 48]
# grades = [calculate_grade(score) for score in scores]

# print(f"Scores: {scores}")
# print(f"Grades: {grades}")


# Autumn = ['September', 'October', 'November']
# Winter = ['December', 'January', 'February']
# Spring = ["March", "April", "May"]
# Summer = ["June", "July", "August"]
# # Collect user input abd capiterlize the first letter
# month = input("Enter current month: ").capitalize()

# if month in Autumn:
#     print("We are in Autumn")
# elif month in Winter:
#     print("We are in Winter")
# elif month in Spring:
#     print("We are in Spring")
# elif month in Summer:
#     print("We are in Summer")

# else:
#     print("Enter Valid month")


# fruit = input("Enter a fruit name: ")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# if fruit in fruits:
#     print("That fruit alredy exist in the list")
# else:
#     fruits.append(fruit)
#     print(f"Fruit list after adding {fruit}: ", fruits)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


person_keys = person.keys()

middle_skills = len(person['skills'])//2

if "skills" in person_keys:
    print(person['skills'][middle_skills])


if "skills" in person_keys and "Python" in person['skills']:
    print(person['skills'])


# Determine the person's title based on their skills
if set(person['skills']) == {'JavaScript', 'React'}:
     print('He is a front end developer')
elif set(person['skills']) == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend developer')
elif set(person['skills']) == {'React', 'Node', 'MongoDB'}:
    print('He is a fullstack developer')
else:
    print('unknown title')   

if person['is_marred'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}, He is Married")