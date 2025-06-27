# Project #1: Quarter of the Year

# Prompt user for a month as a number between 1 and 12
userInput = int(input("Please enter a month as a number between 1 and 12: "))

# if, elif, and else branches
if userInput > 0 and userInput < 13:
    if userInput >= 1 and userInput <= 3:
        print("The month is in the first quarter.")
    elif userInput >= 4 and userInput <= 6:
        print("The month is in the second quarter.")
    elif userInput >= 7 and userInput <= 9:
        print("The month is in the third quarter.")
    elif userInput >= 10 and userInput <= 12:
        print("The month is in the fourth quarter.")
else:
    print("Invalid number! Please enter a number between 1 and 12 only!")


# Project #2: Hot Dog Cookout Calculator

# I need to import math library for .ceil() function to round up for package
import math

# Variable declared and initialized
hotdogs = 10
buns = 8

# Prompt user for a number of people attending the cookout and the number
# of hot dogs each person will be given.
userInputPeople = int(input("Please enter a number of people attending the cookout: "))
userInputHotdogs = int(input("Please enter a number of hot dogs each person will be given: "))

# Calculation
total = userInputPeople * userInputHotdogs
totalPackageHotdog =  math.ceil(total / hotdogs)
totalPackageBuns = math.ceil(total / buns)
totalLeftoverHotdog = (hotdogs * totalPackageHotdog) - total
totalLeftoverBuns = (buns * totalPackageBuns) - total

# Final Output
print(f"You'll need to produce {total} hotdogs; therefore, You'll need {totalPackageHotdog} package(s)\n" +
      f"of hotdogs and {totalPackageBuns} package(s) of buns.")
print(f"There are {totalLeftoverHotdog} hotdog(s) and {totalLeftoverBuns} bun(s) remaining!")


# Project #3: Software Sales

# Variable declared and initialized
package = 99.00

# Prompt users to input their number of packages purchased.
userInput = int(input("Please enter a number of packages purchased: "))

# if, elif, and else branches
if userInput >= 10 and userInput <= 19:
    discount = 0.10
elif userInput >= 20 and userInput <= 49:
    discount = 0.20
elif userInput >= 50 and userInput <= 99:
    discount = 0.30
elif userInput >= 100:
    discount = 0.40
else:
    discount = 0

# Small calculation for discount
total = (package * userInput)
discountPrice = (total * discount)
result = total - discountPrice

# Final output
print(f"Your discount is {discount * 100:.0f}%. Total discount is ${discountPrice:.2f}.")
print(f"Your total amount of the purchase after the discount is ${result:.2f}.")

