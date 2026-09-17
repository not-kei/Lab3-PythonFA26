#Olivia Dodds
#Python FA2026
#Due: Sept 29
#Lab 3: String Spaces
#Takes a string representing a phrase as a parameter and returns the phrase with the 
#order of the letters intact but the spaces between each word are removed.

#ask user for phrase
myString = input("Enter a phrase: ")

#Index starts at 0 to look at the first letter in the phrase
index = 0

#while loop to check each letter in the phrase
while index < len(myString):
    #if the letter is a space, remove it from the phrase
    if myString[index] == " ":
        myString = myString[:index] + myString[index + 1:]
    #if the letter is not a space, move on to the next letter
    else:
        index += 1

#Print the phrase with the spaces removed
print(myString)