# Exercises: Level 1

def add_two_numbers(num1, num2):
    return num1 + num2


print(add_two_numbers(2, 4))


def area_of_circle(r):
    return (3.1415 * r**2)


print(area_of_circle(20))


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f'parameter {num} is not a number')
    return total


print(add_all_nums(2, 3, 4, 2.3, 'man'))


def convert_celsius_to_fahrenheit(c):
    return (c * 9/7 + 32)


print(convert_celsius_to_fahrenheit(-20))

seasons = {
    "Autumn": ['september', 'october', 'november'],
    "Winter": ['december', 'january', 'february'],
    "Spring": ["march", "april", "may"],
    "Summer": ["june", "july", "august"],
}


def check_season(month):
    month = month.lower()
    for season, month_list in seasons.items():
        if month in month_list:
            return season

    return "month not found in any season"


print(check_season("april"))


def calculate_slope(x1, y1, x2, y2):
    try:
        slope = (y2 - y1) / (x2 - x1)
        return slope
    except ZeroDivisionError:
        print("Error: Division by zero. The line is vertical, and the slope is undefined.")


x1, y1 = 1, 2
x2, y2 = 3, 4
slope = calculate_slope(x1, y1, x2, y2)

if slope is not None:
    print(f"The slope of the line is: {slope}")


def print_list(list):
    for item in list:
        print(item)


print(print_list([1, 2, 3, 4, 5, 6, 7]))


def reverse_list(arr):
    revers = arr[::-1]
    return revers


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


def capitalize_list_items(list):
    uppercase_list = [item.upper() for item in list]
    return uppercase_list


print(capitalize_list_items(["a", "b", "c"]))


def add_item(items, to_add):
    items.append(to_add)
    return items


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


def remove_item(items, to_remove):
    modified_lst = [item for item in items if item != to_remove]
    return modified_lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


def sum_of_numbers(num):
    total_sum = sum(range(1, num + 1))
    return total_sum


print(sum_of_numbers(5))


def sum_of_odd(num):
    odd_sum = sum(x for x in range(1, num + 1) if x % 2 != 0)
    return odd_sum


def sum_of_even(num):
    even_sum = sum(x for x in range(1, num + 1) if x % 2 == 0)
    return even_sum


num_example = 10

sum_of_odds_result = sum_of_odd(num_example)
sum_of_even_result = sum_of_even(num_example)

print(sum_of_even_result)
print(sum_of_odds_result)


def evens_and_odds(num):
    even = [x for x in range(1, num ) if x % 2 == 0]
    odd = [x for x in range(1, num ) if x % 2 != 0]

    return f"The number of odds are {len(odd)} \n The Number of evens are {len(even)}"


print(evens_and_odds(10))


def is_empty(arg):
    if len(arg) == 0:
        return "the paramter is empty"
    return f'the parameter as {len(arg)} items'

print(is_empty([1,2,3,4]))


from statistics import mean, median, mode, stdev

def calculate_mean(input_list):
    return mean(input_list)

def calculate_mode(input_list):
    return mode(input_list)
    
def calculate_median(input_list):
    return median(input_list)    

def calculate_range(input_list):
    return max(input_list) - min(input_list)


def calculate_variance(input_list):
     n = len(input_list)
     mean_value = mean(input_list)
     return sum((x - mean_value) ** 2 for x in input_list) / (n - 1)


def calculate_std(input_list):
    return stdev(input_list)



data = [1, 2, 2, 3, 4, 4, 4, 5]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))




def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
    - number: The input number to check.

    Returns:
    True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def are_all_unique(lst):
    """
    Check if all items in a list are unique.

    Parameters:
    - lst: The input list.

    Returns:
    True if all items are unique, False otherwise.
    """
    return len(lst) == len(set(lst))


def are_all_same_type(lst):
    """
    Check if all items in a list are of the same data type.

    Parameters:
    - lst: The input list.

    Returns:
    True if all items are of the same data type, False otherwise.
    """
    return all(isinstance(item, type(lst[0])) for item in lst)


def is_valid_python_variable(variable):
    """
    Check if a provided variable is a valid Python variable.

    Parameters:
    - variable: The input variable.

    Returns:
    True if the variable is a valid Python variable, False otherwise.
    """
    import re
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None
