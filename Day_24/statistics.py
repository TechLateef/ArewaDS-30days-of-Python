                         ###==> Statistics <==###

# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. 
# Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part.
# After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decisions based on data, data tells as they say.


 
                                     ###==> Data <==###
#########################################################################################################
# What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis.
# It can be any character, including text and numbers, pictures, sound, or video. If data is not put in a context, it doesn't make any sense to a human or computer. 
# To make sense from data we need to work on the data using different tools.

# The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created.
# There are structured and unstructured data.

# Data can be found in small or big format.
# Most of the data types we will get have been covered in the file handling section.
#####################################################################################################################




                                          ###==> Statistics Module <==###
#############################################################################################################################################################################################
# The Python statistics module provides functions for calculating mathematical statistics of numerical data.
# The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab.
# It is aimed at the level of graphing and scientific calculators.
######################################################################################################################################################################################################

#

     
                                               ####==> NumPy <==####
######################################################################################################################################
# In the first section we defined Python as a great general-purpose programming language on its own, but with the help of other popular libraries as(numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.

# NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.
###############################################################################################################################################


# Creating numpy array using
# Creating int numpy arrays

#     # Creating python List
#     python_list = [1,2,3,4,5]

#     # Checking data types
#     print('Type:', type (python_list)) # <class 'list'>
#     #
#     print(python_list) # [1, 2, 3, 4, 5]

#     two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

#     print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#     # Creating Numpy(Numerical Python) array from python list

#     numpy_array_from_list = np.array(python_list)
#     print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
#     print(numpy_array_from_list) # array([1, 2, 3, 4, 5])


# Creating float numpy arrays

# Creating a float numpy array from list with a float data type parameter

#     # Python list
#     python_list = [1,2,3,4,5]

#     numy_array_from_list2 = np.array(python_list, dtype=float)
#     print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])




# Converting numpy array to list

# # We can always convert an array back to a python list using tolist().
# np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# How to reverse the rows and the whole array?

# two_dimension_array[::]

#     array([[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]])

# Reverse the row and column positions

#     two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
#     two_dimension_array[::-1,::-1]


#########################################################
    # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
#     numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
#     numpy_zeroes

#     array([[0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0]])

# # Numpy Zeroes
# numpy_ones = np.ones((3,3),dtype=int,order='C')
# print(numpy_ones)

#     [[1 1 1]
#      [1 1 1]
#      [1 1 1]]
#################################################################

# Matrix in numpy

# four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))

# four_by_four_matrix

# matrix([[1., 1., 1., 1.],
#             [1., 1., 1., 1.],
#             [1., 1., 1., 1.],
#             [1., 1., 1., 1.]])

# np.asarray(four_by_four_matrix)[2] = 2
# four_by_four_matrix

# matrix([[1., 1., 1., 1.],
#             [1., 1., 1., 1.],
#             [2., 2., 2., 2.],
#             [1., 1., 1., 1.]])


###############################################################################


# Numpy numpy.arange()
# What is Arrange?

# Sometimes, you want to create values that are evenly spaced within a defined interval. For instance, you want to create values from 1 to 10; you can use numpy.arange() function

# # creating list using range(starting, stop, step)
# lst = range(0, 11, 2)
# lst

# range(0, 11, 2)

# for l in lst:
#     print(l)

#     2
#     4
#     6
#     8
#     10


# Similar to range arange numpy.arange(start, stop, step)
# whole_numbers = np.arange(0, 20, 1)
# whole_numbers

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#            17, 18, 19])

# natural_numbers = np.arange(1, 20, 1)
# natural_numbers

# odd_numbers = np.arange(1, 20, 2)
# odd_numbers

#     array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

# even_numbers = np.arange(2, 20, 2)
# even_numbers

#     array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])

###########################################################################################



# Creating sequence of numbers using linspace

# # numpy.linspace()
# # numpy.logspace() in Python with Example
# # For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
# np.linspace(1.0, 5.0, num=10)

#     array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
#            3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])

# # not to include the last value in the interval
# np.linspace(1.0, 5.0, num=5, endpoint=False)

# array([1. , 1.8, 2.6, 3.4, 4.2])

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

# np.logspace(2, 4.0, num=4)

# array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])

# # to check the size of an array
# x = np.array([1,2,3], dtype=np.complex128)

# x

#     array([1.+0.j, 2.+0.j, 3.+0.j])

# x.itemsize

# 16

# # indexing and Slicing NumPy Arrays in Python
# np_list = np.array([(1,2,3), (4,5,6)])
# np_list

#     array([[1, 2, 3],
#            [4, 5, 6]])

# print('First row: ', np_list[0])
# print('Second row: ', np_list[1])

#     First row:  [1 2 3]
#     Second row:  [4 5 6]

# print('First column: ', np_list[:,0])
# print('Second column: ', np_list[:,1])
# print('Third column: ', np_list[:,2])

#     First column:  [1 4]
#     Second column:  [2 5]
#     Third column:  [3 6]


                        ###==> NumPy Statistical Functions with Example <==###
 
######################################################################################################################

# NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile,standard deviation and variance, etc from the given elements in the array. The functions are explained as follows − Statistical function Numpy is equipped with the robust statistical function as listed below

#     Numpy Functions
#         Min np.min()
#         Max np.max()
#         Mean np.mean()
#         Median np.median()
#         Varience
#         Percentile
#         Standard deviation np.std()


# print(two_dimension_array)
# print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
# print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
# print('=== Row ==')
# print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
# print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

# [[ 1  2  3]
#  [ 4 55 44]
#  [ 7  8  9]]
# Column with minimum:  [1 2 3]
# Column with maximum:  [ 7 55 44]
# === Row ==
# Row with minimum:  [1 4 7]
# Row with maximum:  [ 3 55  9]


# How to create repeating sequences?

# a = [1,2,3]

# # Repeat whole of 'a' two times
# print('Tile:   ', np.tile(a, 2))

# # Repeat each element of 'a' two times
# print('Repeat: ', np.repeat(a, 2))

# Tile:    [1 2 3 1 2 3]
# Repeat:  [1 1 2 2 3 3]


# print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# ['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']

# ['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']

# ['iueoaieuoi']


# from scipy import stats
# np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
# np_normal_dis
# ## min, max, mean, median, sd
# print('min: ', np.min(np_normal_dis))
# print('max: ', np.max(np_normal_dis))
# print('mean: ', np.mean(np_normal_dis))
# print('median: ', np.median(np_normal_dis))
# print('mode: ', stats.mode(np_normal_dis))
# print('sd: ', np.std(np_normal_dis))

#     min:  3.557811005458804
#     max:  6.876317743643499
#     mean:  5.035832048106663
#     median:  5.020161980441937
#     mode:  ModeResult(mode=array([3.55781101]), count=array([1]))
#     sd:  0.489682424165213

# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()



# Linear Algebra

#     Dot Product

# ## Linear algebra
# ### Dot product: product of two arrays
# f = np.array([1,2,3])
# g = np.array([4,5,3])
# ### 1*4+2*5 + 3*6
# np.dot(f, g)  # 23



# NumPy Matrix Multiplication with np.matmul()

# ### Matmul: matruc product of two arrays
# h = [[1,2],[3,4]]
# i = [[5,6],[7,8]]
# ### 1*5+2*7 = 19
# np.matmul(h, i)

#     array([[19, 22],
#            [43, 50]])

###########################################################################################