# Packing Dictionaries

# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
#     # Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))

# name = Asabeneh
# country = Finland
# city = Helsinki
# age = 250
# {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
# Sometimes we would like to combine lists when looping through them. See the example below:

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)

# ames = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
#  Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.                                                                                                   
ames = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

nordic_countries = ames[:5]
print(nordic_countries)
es = ames[5:6]
print(es)
ru = ames[6:7]
print(ru)