#Olivia Dodds
#Python FA2026
#Due: Sept 29
#Lab 3: Grades
#Takes a numeric grade from the user and outputs the corresponding letter grade. 
#Checks if the grade is valid and prints an error message if it is not.

#ask user for grade
grade = float(input("Enter your grade: "))

#check if grade is valid
if grade > 100 or grade < 0:
    print("Invalid grade. Please enter a grade between 0 and 100.")
#prints the letter grade based on the numeric grade
else:
    if grade >= 90:
        print("You got an A !")
    elif grade >= 80:
        print("You got a B!")
    elif grade >= 70:
        print("You got a C!")
    elif grade >= 60:
        print("You got a D!")
    else:
        print("You got an F!")

