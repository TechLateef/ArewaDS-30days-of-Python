# Exercise 1
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

print('Company lenght: ', len(it_companies))

# ? adding twitter to it_companies

it_companies.add("Twitter")
print("IT companies after adding twitter ", it_companies)

# Addingf multple company

it_companies.update(['Cisco', 'X', 'Digital Ocean'])
print("IT companies after adding multiple company using Update(): ", it_companies)

# Removing one company from it_companies
it_companies.remove('X')

print("It companies after removing one company ", it_companies)
it_companies.discard

#  Differece between remove and discard
# remove() method
# Remove an element from a set; it must be a member.

# If the element is not a member, it raise a KeyError.

# while discard Remove an element from a set if it is a member.

# unlike remove() method, discard() method does not raise an exception when an element is missing from the set.


# Exercise 2

A = {'1', '2', '3'}
B = {'4', '5', '6'}

print('Intersection between set A and B is: ', A.intersection(B))
print('Is A a Subset of B: ', A.issubset(B))
print('Are A and B disjoint set: ', A.isdisjoint(B))


print("Joining A with B: ", A.union(B))
print("Joining B with A: ", B.union(A))

print('The Symmetric difference between A and B: ', A.symmetric_difference(B))

del A, B

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)

print('Age as set:{}  and it lenght: {}'.format(age_set, len(age_set)))
print('Age as list:{}  and it lenght: {}'.format(age, len(age)))


# Explain the difference between the following data types: string, list, tuple and set

# String: Immutable. You cannot modify the content of a string once created and also The characters in a string have a specific order that cannot be changed.
# List: Mutable. You can add, remove, or modify elements of a list after its creation. and The elements in a list maintain the order in which they were added.
# Tuple: Immutable. Similar to strings, tuples cannot be changed after creation. Similar to lists, the elements in a tuple maintain their order.
# Set: Mutable (partially). You can add or remove elements from a set, but you cannot modify existing elements. lements in a set do not have a specific order and may appear in different orders when accessed

sentence = "I am a teacher and I love to inspire and teach people."

# Split the sentence into words
words = sentence.split()

# Convert the words to lowercase (for case-insensitive comparison)
words = [word.lower() for word in words]

unique_words = set(words)
print('Unique words: ', unique_words)
#  Number of unique words
print('Number of unique words: ', len(unique_words))
