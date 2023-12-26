# Pandas data structure is based on Series and DataFrames.

# A series is a column and a DataFrame is a multidimensional table made up of collection of series.
# In order to create a pandas series we should use numpy to create a one dimensional arrays or a python list

# Creating Pandas Series with Default Index

# nums = [1, 2, 3, 4,5]
# s = pd.Series(nums)
# print(s)
#   0    1
#     1    2
#     2    3
#     3    4
#     4    5
#     dtype: int64


# Creating Pandas Series with custom index

# nums = [1, 2, 3, 4, 5]
# s = pd.Series(nums, index=[1, 2, 3, 4, 5])
# print(s)

#     1    1
#     2    2
#     3    3
#     4    4
#     5    5
#     dtype: int64



# Creating Pandas Series from a Dictionary

# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

# s = pd.Series(dct)
# print(s)

#     name       Asabeneh
#     country     Finland
#     city       Helsinki
#     dtype: object



# Creating a Constant Pandas Series

# s = pd.Series(10, index = [1, 2, 3])
# print(s)

#     1    10
#     2    10
#     3    10
#     dtype: int64

# Creating a Pandas Series Using Linspace

# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)

#     0     5.000000
#     1     6.666667
#     2     8.333333
#     3    10.000000
#     4    11.666667
#     5    13.333333
#     6    15.000000
#     7    16.666667
#     8    18.333333
#     9    20.000000
#     dtype: float64


# DataFrames

# Pandas data frames can be created in different ways.
# Creating DataFrames from List of Lists

# data = [
#     ['Asabeneh', 'Finland', 'Helsink'], 
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# df = pd.DataFrame(data, columns=['Names','Country','City'])
# print(df)



# data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
#     'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
# df = pd.DataFrame(data)
# print(df)


# data = [
#     {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
#     {'Name': 'David', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
# df = pd.DataFrame(data)
# print(df)



# Let us also explore the last recordings of the dataframe using the tail() methods.

# print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method


# As you can see the csv file has three rows: Gender, Height and Weight. If the DataFrame would have a long rows, it would be hard to know all the columns. Therefore, we should use a method to know the colums. we do not know the number of rows. Let's use shape meathod.

# print(df.shape) # as you can see 10000 rows and three columns

# (10000, 3)


# Let us get all the columns using columns.

# print(df.columns)

# Index(['Gender', 'Height', 'Weight'], dtype='object')

# Now, let us get a specific column using the column key

# heights = df['Height'] # this is now a series

# print(heights)


# The describe() method provides a descriptive statistical values of a dataset.

# print(heights.describe()) # give statisical information about height data

#     count    10000.000000
#     mean        66.367560
#     std          3.847528
#     min         54.263133
#     25%         63.505620
#     50%         66.318070
#     75%         69.174262
#     max         78.998742
#     Name: Height, dtype: float64


# print(df.describe())  # describe can also give statistical information from a dataFrame



                        ###==> Modifying a DataFrame <==###
###########################################################################################################################################################
# Modifying a DataFrame: * We can create a new DataFrame * We can create a new column and add it to the DataFrame, * we can remove an existing column from a DataFrame, * we can modify an existing column in a DataFrame, * we can change the data type of column values in the DataFrame
# Creating a DataFrame

# As always, first we import the necessary packages. Now, lets import pandas and numpy, two best friends ever.

# import pandas as pd
# import numpy as np
# data = [
#     {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
#     {"Name": "David", "Country":"UK","City":"London"},
#     {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
# df = pd.DataFrame(data)
# print(df)

# Adding a New Column

# Let's add a weight column in the DataFrame

# weights = [74, 78, 69]
# df['Weight'] = weights
# df


# Using functions makes our code clean, but you can calculate the bmi without one
# def calculate_bmi ():
#     weights = df['Weight']
#     heights = df['Height']
#     bmi = []
#     for w,h in zip(weights, heights):
#         b = w/(h*h)
#         bmi.append(b)
#     return bmi
    
# bmi = calculate_bmi()

# df['BMI'] = bmi
# df

##################################################################################################################################################################################################################################################


