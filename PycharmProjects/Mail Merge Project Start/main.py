
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

str="[name]"
with open("Input/Names/invited_names.txt") as namefile:
    names =namefile.readlines()
with open("Input/Letters/starting_letter.txt") as letters:
     letter=letters.read()
     print(letter)

     for name in names:
             stripped=name.strip()
             new_content = letter.replace(str, stripped)
             print(new_content)
             create=open(f"./Output/ReadyToSend/letter_for_{stripped}.txt", mode="w")
             create.write(letter)
#