
print('Thirty ' + 'Days '+ 'Of '+'Python')
print('Coding ' + 'For '+ 'All ')
company = "Coding For All"
print(company)
print(len(company))
print("company in Upper case: ", company.upper())
print("company in lower case: ", company.lower())
print("company with capitalize: ", company.capitalize())
print("company with title: ", company.title())
print("company with swap: ", company.swapcase())
first_word = company[0:6]
print("cut the first word from company: ",first_word )
sub_string ="Coding"
print(" company contains coding: ", company.find(sub_string))
print("replacing Coding with Python: ", company.replace("Coding","Python"))
replace_word ="Python for Everyone"
print(f"changing {replace_word} to: Python for all  ", replace_word.replace(replace_word, "Python for All "))
print("Spliting using split() Method: ", company.split())

words = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print('spliting from comma: ', words.split(', '))

print("Character at index 0: ",  company[0])
print("Character at last index : ",  company[-1])
pfe_word ="Python For Everyone"
cfa= " ".join(word[0].upper() for word in company.split())
print(" abbreviation for the name Coding For All: ", cfa)

pfe= " ".join(word[0].upper() for word in pfe_word.split())
print(" abbreviation for the name Python For Everyone: ", pfe)

print(f"First occurrence of c in {company} ", company.index("C"))

print(f"First occurrence of F in {company} ", company.index("F"))
print(f"Last occurrence of l in {company} ", company.rindex("l"))

find_word = 'You cannot end a sentence with because because because is a conjunction'

print("finding the first occurrence of the word because", find_word.find("because"))
print("finding the last occurrence of the word because", find_word.rindex("because"))

word_to_slice_from =  'You cannot end a sentence with because because because is a conjunction'
print("Slicing out the word because", word_to_slice_from.replace("because", ""))

print(f"finding the first occurence of the word {word_to_slice_from} ", word_to_slice_from.find("because"))

print("Does ''Coding For All' start with a substring Coding?: ", company.startswith("Coding"))

print("Does ''Coding For All' end with a substring coding?: ", company.startswith("coding"))


words_strip ='   Coding For All      '

print(f"removing space from the word", words_strip.strip(" "))

id = '30DaysOfPython'
id2="thirty_days_of_python"
print("30DaysOfPython", id.isidentifier())
print("thirty_days_of_python", id2.isidentifier())


python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(" #".join(python_lib))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t      Age\t     Country\t   City\t \nAsabeneh\t 250\t Finland\t Helsinki\t")


radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = f'The area of circle with a radius {radius} is {area} meters square'

print(formated_string)

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))