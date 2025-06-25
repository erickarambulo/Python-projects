# Project #1

# Ask user to input their temperature
temperature = int(input("Please enter the temperature: "))

# if and else branches
if temperature < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having.")


# Project #2

# Ask users to input their number for sales
sales = int(input("Please enter the number of sales: "))

# if and else branches
if sales > 50000:
    bonus = 500.0
    commission_rate = 0.12
    print("You met your sales quota!")


# Project #3

# Ask users to input their number within the range of 1 to 10
number = int(input("Please enter your number within the range of 1 - 10: "))

# if, elif, and else branches
if number == 1:
    print(f"Roman Numeral for {number} is I.")
elif number == 2:
    print(f"Roman Numeral for {number} is II.")
elif number == 3:
    print(f"Roman Numeral for {number} is III.")
elif number == 4:
    print(f"Roman Numeral for {number} is IV.")
elif number == 5:
    print(f"Roman Numeral for {number} is V.")
elif number == 6:
    print(f"Roman Numeral for {number} is VI.")
elif number == 7:
    print(f"Roman Numeral for {number} is VII.")
elif number == 8:
    print(f"Roman Numeral for {number} is VIII.")
elif number == 9:
    print(f"Roman Numeral for {number} is IX.")
elif number == 10:
    print(f"Roman Numeral for {number} is X.")
else:
    print("Invalid number! Please only enter from 1 - 10!")


# Project #4

# Prompt an user to input their grade score
firstTestScore = int(input("Please enter a number from 0 to 25 for student's score on 1st test: "))
secondTestScore = int(input("Please enter a number from 0 to 25 for student's score on 2nd test: "))
mainTestScore = int(input("Please enter a number from 0 to 50 for student's score on main test: "))

# Add 3 tests into total
totalScore = firstTestScore + secondTestScore + mainTestScore

# if, elif, and else branches
if (firstTestScore >= 0 and firstTestScore < 26) and (secondTestScore >=0 and secondTestScore < 26) and (mainTestScore >= 0 and mainTestScore <= 50):
    if (totalScore < 50) or (mainTestScore < 25):
        print(f"your total score is {totalScore}.")
        print("Fail")
    elif totalScore > 80 and totalScore <= 100:
        print(f"your total score is {totalScore}.")
        print("Distinction")
    elif totalScore > 60 and totalScore <= 100:
        print(f"your total score is {totalScore}.")
        print("Credit")
    elif totalScore < 60:
        print(f"your total score is {totalScore}.")    
        print("Pass")
else:
    print("Invalid grade score! Please try again!")


# Project #5

# Prompt user to enter their number from 0 to 36
from zmq import RATE


pocket = int(input("Enter your number from 0 to 36: "))

# if, elif, and else branches
if (pocket >= 0 and pocket <= 36):    
    if pocket == 0:
        print("Your color is green!")
    elif pocket > 0 and pocket < 11:
        if pocket % 2 == 1:
            print("Your color is red!")
        else:
            print("Your color is black!")
    elif pocket > 10 and pocket < 19:
        if pocket % 2 == 1:
            print("Your color is black!")
        else:
            print("Your color is red!")
    elif pocket > 18 and pocket < 29:
        if pocket % 2 == 1:
            print("Your color is red!")
        else:
            print("Your color is black!")
    elif pocket > 28 and pocket < 37:
        if pocket % 2 == 1:
            print("Your color is black!")
        else:
            print("Your color is red!")
else:
    print("Invalid number! Please enter 0 to 36 only!")


# Project #6

# Prompt user to enter the weight of a package then displays the
# shipping charges.
userInput = float(input("Please enter the weight of a package: "))

# if, elif, and else branches
if userInput <= 2:
    ratePerPound = 1.50
elif userInput > 2 and userInput <= 6:
    ratePerPound = 3.00
elif userInput > 6 and userInput <= 10:
    ratePerPound = 4.00
elif userInput > 10:
    ratePerPound = 4.75

# calculation
total = userInput * ratePerPound
print(f"Your total is ${total:.2f}.")

