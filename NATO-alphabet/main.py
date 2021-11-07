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
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#creating a nato_data object from the csv doc 
nato_data =pandas.read_csv('nato_phonetic_alphabet.csv') 
# print(nato_data) #SANITY CHECK

nato_data_dict = {} #create a blank dict to be updated by for loop NOT REQUIRED WITH DICT COMP


#iterring through a datatframe using the iterrows() to go by row instead of going by columns. USe row.name_of_column to get the data from correpsonding rows 
for (index, row ) in nato_data.iterrows():
    # print(row.letter) #SANITY CHECK 
    # print(row.code)  #SANITY CHECK 
    nato_data_dict.update({row.letter:row.code})
# print(nato_data_dict)  #SANITY CHECK 



#same actvity but using dict coprehension BELOW 

new_comp_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(new_comp_dict) #SANITY CHECK
 
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input('please provide a word: ')
# phonetic_alphabet =[]
# for letter in word:
#     letter = letter.upper()
#     # print(letter) #SANITY CHECK
#     if letter in  new_comp_dict.keys():
#         # print('letter found ') #SANITY CHECK
#         # print(new_comp_dict[letter]) #SANITY CHECK 
#         phonetic_alphabet.append(new_comp_dict[letter])
# print(phonetic_alphabet)


# TODO 2 altrative to the ocde using dict comprehension 
word2 =input('provide another word: ').upper()
output = [new_comp_dict[letter] for letter in word2]
print(output)
    

