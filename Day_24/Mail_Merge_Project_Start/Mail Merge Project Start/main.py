#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('Input\Letters\starting_letter.txt') as file:
    letter_data = file.read()

with open('Input/Names/invited_names.txt') as file:
    list_of_name = file.read()
list_of_name = list_of_name.split('\n')

for i in list_of_name:
    data = letter_data.replace('[name]', i)
    with open(f'Output/ReadyToSend/letter_for_{i}.txt', 'w') as file:
        file.write(data)
#data =data.replace('[name]','ritik')
#
#with open('Output/ritik.txt','w') as file:
#    file.write(data)