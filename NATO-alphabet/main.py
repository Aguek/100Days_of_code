
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    dict_key = key
    dict_val = value

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    dict_index = index
    dict_row = row
    #Access row.student or row.score
    student = row.student
    score = row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
csv_file = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in csv_file.iterrows()}

# for (index, row) in csv_file.iterrows():
#     print(row.letter)
#     print(row.code)

# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word.").upper()

# solution using a for loop
# for letter in word:
#     for (key, value) in new_dict.items():
#         if letter in key:
#             new_list.append(value)
# print(new_list)
# solution using dict comprehensions

new_list = [new_dict[letter] for letter in word]
print(new_list)

