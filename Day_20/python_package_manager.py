# import webbrowser
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# for url in url_lists:
#     webbrowser.open_new_tab(url)


# To open a network connection, we need a package called requests - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations.
# In this section, we will cover only reading ore getting part of a CRUD.

    # get(): to open a network and fetch data from url - it returns a response object
    # status_code: After we fetched data, we can check the status of the operation (success, error, etc)
    # headers: To check the header types
    # text: to extract the text from the fetched response object
    # json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.



import requests

# url =  'https://www.w3.org/TR/PNG/iso_8859-1.txt'

# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)


############################################################################################################################################
# Let us read from an API. API stands for Application Program Interface. 
# It is a means to exchange structure data between servers primarily a json data. An example of an API:https://restcountries.eu/rest/v2/all.
#  Let us read this API using requests module.
###############################################################################################################################################
# url = 'https://restcountries.eu/rest/v2/all' 
# response = requests.get(url)
# print(response)
# print(response.status_code)
# countries = response.json()
# print(countries[:1])

################################################################################
# We use json() method from response object, if the we are fetching JSON data.
#  For txt, html, xml and other file formats we can use text
#################################################################################



#################################################################
# A package is actually a folder containing one or more module files. 
# Let us create a package named mypackage, using the following steps:
#####################################################################


##############################################################################################################
#  The package folder contains a special file called init.py - it stores the package's content.
# If we put init.py in the package folder, python start recognizes it as a package. 
# The init.py exposes specified resources from its modules to be imported to other python files.
# An empty init.py file makes all functions available when a package is imported. The init.py is essential for the folder to be recognized by Python as a package.
########################################################################################################################################################


import re
from  collections import Counter
# Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

def most_common_word(url, numb_word=10):
    response = requests.get(url).text
    # print(response)
    words = response.split()
    clean = [re.sub([r'^/w/s'], '', word.lower()) for word in words]
    word_count = Counter(clean)
    most_common = word_count.most_common(numb_word)
    return most_common




# url = 'http://www.gutenberg.org/files/1112/1112.txt'


# print(most_common_word(obam))


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

#     the min, max, mean, median, standard deviation of cats' weight in metric units.
#     the min, max, mean, median, standard deviation of cats' lifespan in years.
#     Create a frequency table of country and breed of cats

from statistics import median, mean, stdev

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)
print(response)
print(response.status_code)
# print(response.json())
cats = response.json()
# print(cats[:])

ind = [cat['weight']['metric'] for cat in cats]
weight = [sum(map(int, pair.split(' - ')))/2 for pair in ind]
print("################################ weight")

print(weight)
print("Min: ",min(weight))
print("Max: ",max(weight))
print("Median: ", median(weight))
print('Mean: ', mean(weight))
print("Standard deviation: ", stdev(weight))



print("################################ life span")
life_spans = [cat['life_span'] for cat in cats]
life_span = [sum(map(int, pair.split(' - ')))/2 for pair in life_spans]
print(life_span)

print("Min: ",min(life_span))
print("Max: ",max(life_span))
print("Median: ", median(life_span))
print('Mean: ', mean(life_span))
print("Standard deviation: ", stdev(life_span))


coutries = [cat['origin'] for cat in cats]

print(coutries)