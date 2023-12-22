# Regular Expressions

# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type.
# To use RegEx in python first we should import the RegEx module which is called re.

# The re Module

# After importing the module we can use it to detect or find patterns.

# import re



# Methods in re Module

# To find a pattern we use different set of re character sets that allows to search for a match in a string.

#     re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
#     re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
#     re.findall: Returns a list containing all matches
#     re.split: Takes a string, splits it at the match points, returns a list
#     re.sub: Replaces one or many matches within a string

# syntac
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern ,
#  re.I is case ignore

# import re

# txt = 'I love to teach python and javaScript'
# # It returns an object with span, and match
# match = re.match('I love to teach', txt, re.I)
# print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (0, 15)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 0, 15
# substring = txt[start:end]
# print(substring)       # I love to teach


# As you can see from the example above, the pattern we are looking for (or the substring we are looking for) is I love to teach.
# The match function returns an object only if the text starts with the pattern.


# import re

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first

# As you can see, search is much better than match because it can look for the pattern throughout the text. Search returns a match object with a first match that was found, otherwise it returns None. A much better re function is findall. 
# This function checks for the pattern through the whole string and returns all the matches as a list.

# Searching for All Matches Using findall

# findall() returns all the matches as a list

import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


paragraph = paragraph.lower()
paragraph = re.sub(r'[^\w\s]', '', paragraph)  


words = paragraph.split()
word_counts = Counter(words)

word_frequencies = word_counts.most_common()

print(word_frequencies)


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
 # Extract numbers with optional negative sign
# Regular Expression: r'-?\d+' matches one or more digits (\d+) with an optional negative sign (-?).
numbers = re.findall(r'-?\d+', text) 
points = [int(num) for num in numbers]
 # Sort in ascending order
points.sort() 
# Subtract the smallest from the largest
distance = points[-1] - points[0]  

print("Distance between furthest particles:", distance)  # Output: 20

# []: Character Class

#     It creates a set of allowed characters for a particular position in the pattern.
#     It matches any single character that belongs to the defined set.

#  ^ Inside Character Class: Negation

#     When placed within a character class, 
#     ^ inverts the meaning, indicating which characters are not allowed.
#     It matches any character that is not one of the specified characters within the class.

def is_valid_variable(arg):
     pattern = r"^[^\d\W]\w*$"  
     return bool(re.match(pattern, arg))



print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))



def clean_text(text):
  """Cleans text by removing special characters and extra whitespace."""
  # Remove special characters
  cleaned_text = re.sub(r"[^\w\s]", "", text)  
  # Normalize whitespace
  cleaned_text = re.sub(r"\s+", " ", cleaned_text)  
  # Convert to lowercase
  return cleaned_text.lower()  

def most_frequent_words(text, top_n=3):
  """Returns the top n most frequent words in the text."""
  words = text.split()
  word_counts = Counter(words)
  return word_counts.most_common(top_n)


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
most_frequent = most_frequent_words(cleaned_text)

print(cleaned_text)
print(most_frequent)