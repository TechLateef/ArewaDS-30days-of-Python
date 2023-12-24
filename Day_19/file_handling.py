# Write a function which count number of lines and number of words in a text. 
# All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.
# txt file and count number of lines and words


def count_line_and_words(file_path):
    with open(file_path) as f:
        lines =   f.read().splitlines()
        num_lines = len(lines)
        words = 0
        for line in lines:
            words += len(line.split())    
    return {"lines":num_lines, "word": words }

obama_speech = "../data/obama_speech.txt"
michelle_obama_speech = "../data/michelle_obama_speech.txt"
melina_trump_speech = "../data/melina_trump_speech.txt"


print("obama_speech: ",count_line_and_words(obama_speech))

print("michelle_obama_speech: ",count_line_and_words(michelle_obama_speech))

print("melina_trump_speech: ",count_line_and_words(melina_trump_speech))




import json
from collections import Counter

def most_spoken_languages(filename, top_n=10):
    """Finds the top N most spoken languages in a JSON file."""

    with open(filename, 'r') as file:
        data = json.load(file)

    language_counts = Counter()
    for country in data:
        language_counts.update(country['languages'])

    most_common = language_counts.most_common(top_n)
    return most_common


filename = "../data/countries_data.json"
print(most_spoken_languages(filename, 10))


def most_populated_countries(filename, top_n=10):
    """Finds the top N most populated countries in a JSON file."""

    with open(filename, 'r') as file:
        data = json.load(file)

    countries = sorted(data, key=lambda country: country['population'], reverse=True)
    top_countries = countries[:top_n]  # Get the top N countries

    return [{'country': country['name'], 'population': country['population']} for country in top_countries]



filename = "../data/countries_data_long.json"
print(most_populated_countries(filename, 10))


import os
import re
def find_most_common_words(text_or_filename, num_words):
    if isinstance(text_or_filename, str) and os.path.isfile(text_or_filename):
        with open(text_or_filename, 'r') as file:
            words = file.read().split()
    elif isinstance(text_or_filename, str):
        words = text_or_filename.split()
    else:
        raise ValueError("Invalid input: must be a string or a valid file path")

    # Clean words (remove punctuation, lowercase)
    clean_words = [re.sub(r'[^\w\s]', '', word.lower()) for word in words]

    word_counts = Counter(clean_words)
    most_common = word_counts.most_common(num_words)
    return most_common




print(find_most_common_words("This is a string with some words to analyze.", 5))

print(find_most_common_words(obama_speech, 5))
print(find_most_common_words(michelle_obama_speech, 5))
print(find_most_common_words(melina_trump_speech, 5))





# import re
# from collections import Counter
# from nltk.tokenize import word_tokenize
# from data.stop_words import stop_words  # Import stop words from your file

# def clean_text(text):
#     # Remove non-alphanumeric characters and convert to lowercase
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
#     return cleaned_text

# def remove_stop_words(text, stop_words):
#     words = word_tokenize(text)
#     filtered_words = [word for word in words if word.lower() not in stop_words]
#     return ' '.join(filtered_words)

# def check_text_similarity(text1, text2, stop_words):
#     cleaned_text1 = remove_stop_words(clean_text(text1), stop_words)
#     cleaned_text2 = remove_stop_words(clean_text(text2), stop_words)

#     words1 = cleaned_text1.split()
#     words2 = cleaned_text2.split()

#     # Calculate Jaccard similarity
#     intersection = len(set(words1) & set(words2))
#     union = len(set(words1) | set(words2))
#     similarity = intersection / union

#     return similarity

# if __name__ == "__main__":
#     # Load the text from files or provide your own strings
#     with open(michelle_obama_speech, 'r') as file:
#         michelle_speech = file.read()

#     with open(melina_trump_speech, 'r') as file:
#         melina_speech = file.read()

#     similarity = check_text_similarity(michelle_speech, melina_speech, stop_words)
#     print(f"Similarity between the speeches: {similarity:.2%}")


romeo_words = '../data/romeo_and_juliet.txt'
print(find_most_common_words(romeo_words, 10))


import csv

def count_lines_with_keyword(csv_file, keyword):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        lines_with_keyword = [line for line in reader if keyword.lower() in line[1].lower()]
    return len(lines_with_keyword)



csv_file = '../data/hacker_news.csv'

    # Count lines containing 'python' or 'Python'
python_count = count_lines_with_keyword(csv_file, 'python')

    # Count lines containing 'JavaScript', 'javascript', or 'Javascript'
javascript_count = count_lines_with_keyword(csv_file, 'javascript')

print(python_count)
print(javascript_count)