student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(row.score)
    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_pd=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter:row.code for (index,row) in nato_pd.iterrows()}
#print(dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_dict=[]
word=input("Enter a word").upper()
# for i in word:
#     i=i.upper()
#     if i in dict.keys():
#
#         nato_dict.append(dict[i])
# print(nato_dict)
natodict=[dict[i] for i in word]
print(natodict)