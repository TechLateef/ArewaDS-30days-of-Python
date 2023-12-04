empty_list = []
lst_of_item = [1, 3, 4, 6, 7, 8]
print("length of the list: ", len(lst_of_item))
middle_item = len(lst_of_item)//2
print('first element', lst_of_item[0])
print('last element', lst_of_item[middle_item])
print('last element', lst_of_item[-1])
mixed_data_types = ['Mubarak', 12, 7.0, 'singlet', 'abuja']
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
print('Mixed data type: ', mixed_data_types)
print('IT Companies: ', it_companies)

print("Number of company in the list: ", len(it_companies))

middle_item = len(it_companies)//2
print('first item', it_companies[0])
print('last item', it_companies[middle_item])
print('last item', it_companies[-1])

it_companies[2] = "X"

print("IT company list after modify ", it_companies)

it_companies.append("Samsung")
print("It companies after adding one company ", it_companies)

it_companies.insert(4, "Cisco")

print(it_companies[-1].upper())

print('# '.join(it_companies))
company_to_find = "Google"

if company_to_find in it_companies:
    print(f"{company_to_find} is in the list.")
else:
    print(f"{company_to_find} is not in the list.")


does_exist = "LG" in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

# print the first 3 items 
print(it_companies[0:3])

# the last 3 items
print(it_companies[-3:])

# the miidle items
middle_company = it_companies[1]

print(middle_company)

# remove the first items
del it_companies[0]

print(it_companies)

# remove the second items

del it_companies[1]

print(it_companies)

# remove the last items
it_companies.pop()

print(it_companies)

# remove All items
it_companies.clear()

print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# join the two list
full_stack = front_end + back_end
full_stack.insert(3,'Python '  "Redux")

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages.sort())

print("max age ", max(ages))
print("min age ", min(ages))

# Find min and max age
min_age = ages[0]
max_age = ages[-1]

# Add min and max age to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2] + ages[n//2 + 1]) / 2
else:
    median_age = ages[n//2]

# Find the average age
average_age = sum(ages) / n

# Find the range of ages
age_range = max_age - min_age


# Compare (min - average) and (max - average)
difference = abs(min_age - average_age) - abs(max_age - average_age)

# Find the middle country(ies)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
if n % 2 == 0:
    middle_countries = [countries[n//2], countries[n//2 + 1]]
else:
    middle_countries = [countries[n//2]]

# Divide countries list into two equal lists
first_half, second_half = countries[:n//2], countries[n//2:]

# Unpack the first three countries and the rest as scandic countries
first_three, *scandic_countries = countries[:3]

print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age:.2f}")
print(f"Range: {age_range}")
print(f"Difference: {difference:.2f}")
print(f"Middle country(ies): {middle_countries}")
print(f"First half: {first_half}, Second half: {second_half}")
print(f"First three: {first_three}, Scandic countries: {scandic_countries}")
