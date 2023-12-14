# 💻 Exercises: Day 12

import random
import string

def random_user_id():
    rand_num = random.randint(100000, 999999)
    user_id = str(rand_num)
    return user_id
print(random_user_id());


def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for each user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))

    user_ids = []
    for _ in range(num_ids):
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k = num_characters))
        user_ids.append(random_id)

    return user_ids



print(user_id_gen_by_user())



# Exercises: Level 2
def list_of_hexa_colors(num_colors):
    hexa_colors = ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(num_colors)]
    return hexa_colors

def list_of_rgb_colors(num_colors):
    rgb_colors = ['rgb({}, {}, {})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)]
    return rgb_colors

def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return None
    



hexa_colors_result = generate_colors('hexa', 3)
print(hexa_colors_result)

hexa_colors_result_single = generate_colors('hexa', 1)
print(hexa_colors_result_single)

rgb_colors_result = generate_colors('rgb', 3)
print(rgb_colors_result)

rgb_colors_result_single = generate_colors('rgb', 1)
print(rgb_colors_result_single)


#  Exercises: Level 3

def shuffle_list(input_list):
    shuffled_list = random.sample(input_list, len(input_list))
    return shuffled_list


def generate_unique_numbers():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_result = shuffle_list(original_list)
print("Shuffled List:", shuffled_result)

unique_numbers_result = generate_unique_numbers()
print("Unique Numbers:", unique_numbers_result)

def concatenate_strings(input_list):
    nsingle = ''
    for x in input_list:
        nsingle += x
    return nsingle

input_strings = ["Hello", " ", "World", "!"]
print(concatenate_strings(input_strings))