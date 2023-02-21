student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_data={row.letter:row.code for (index, row) in data.iterrows()}
#Loop through rows of a data frame
    #Access index and row
    #Access row.student or row.score

print(phonetic_data)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Enter a word ").upper())
nato_output = [phonetic_data[i] for i in word]

print(nato_output)


