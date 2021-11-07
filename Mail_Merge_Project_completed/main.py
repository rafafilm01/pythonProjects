#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def listToString(lst):
    str1 =''
    return str1.join(lst)


with open ('./input/letters/starting_letter.txt') as file:
    letter =file.readlines()
    print(letter)

with open ('./input/names/invited_names.txt') as invited_names:
    names =invited_names.readlines()
    print(names)

#loop over all names and use the name to replace letter[0] in the starting_letter
for name in names:
    letter[0] = f'Dear {name}'
    
    #convert the list into a string using custom made function
    converted_letter =listToString(letter)
    
    #strip() method to get rid of the \n from names (only needed  for naming the file as \n is not allowed in the name of the file)
    stripped_name = name.strip()

    # save the personalised letter to output folder , stripped_name is used in the title of the letter
    with open (f'./output/readyToSend/letter_to_{stripped_name}.txt', mode='w') as new_letter:
        new_letter.write(converted_letter)