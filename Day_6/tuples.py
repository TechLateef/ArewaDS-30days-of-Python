# Exercise 1
empty_tuple = ()
sisters_tuple = ("Fatima", "Maryam")
brothers_tuple =("Abdul","Muhammad")
siblings = sisters_tuple+ brothers_tuple
print("Siblings: ", siblings)

print("Number of siblings: ", len(siblings))

add_tuple = ("Abdul","lv")
family_members = siblings + add_tuple
print("Family member: ", family_members)


# Exercise 2

print("parents: ", add_tuple)
print("Silings: ", siblings)
# Create fruits, vegetables and animal products tuples
fruits_tp = ("apple", "banana", "orange")
vegetables_tp = ("potato", "tomato", "onion")
animal_products_tp = ("milk", "egg", "cheese")

# Join the three tuples
food_stuff_tp = fruits_tp + vegetables_tp + animal_products_tp

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    del food_stuff_lt[middle_index:middle_index + 2]
else:
    del food_stuff_lt[middle_index]

# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = food_stuff_lt[3:-3]

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
item_to_find = "cheese"
if item_to_find in food_stuff_lt:
    print(f"{item_to_find} is in the food_stuff_lt list.")
else:
    print(f"{item_to_find} is not in the food_stuff_lt list.")

# Check if 'Estonia' is a nordic country
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
if "Estonia" in nordic_countries:
    print("'Estonia' is a nordic country.")
else:
    print("'Estonia' is not a nordic country.")

# Check if 'Iceland' is a nordic country
if "Iceland" in nordic_countries:
    print("'Iceland' is a nordic country.")
else:
    print("'Iceland' is not a nordic country.")

print(f"Food stuff list after modifications: {food_stuff_lt}")
