# Project #1: How Much Insurance?

# Function defined
def insurance():
    # Ask user for percent on insured
    userInput = float(input("Please enter the replacement cost of a building: $"))
    
    # Calculation
    result = userInput * 0.80

    # Final output
    print(f"\nThe minimum amount of insurance you should buy for the property is ${result:.2f}")

# Calls function
insurance()


# Project #2: Stadium Seating

# Function defined
def stadium_seating(classA, classB, classC):
    # Calculation
    total_profit = (classA * 20.00) + (classB * 15.00) + (classC * 10.00)
    # Final output
    print(f"\nThe amount of income generated from ticket sales is ${total_profit:.2f}")


# Ask an user how many tickets for each class of seats were sold
classA = int(input("How many tickets are sold for Class A seats: "))
classB = int(input("How many tickets are sold for Class B seats: "))
classC = int(input("How many tickets are sold for Class C seats: "))

# Calls function
stadium_seating(classA, classB, classC)


# Project #3: Sum of Numbers - Files and Exceptions

# Variable declared and initialized
total = 0
count = 0

# Open the file
with open("numbers.txt", "r") as file:
    # For loop
    for line in file:
        number = int(line)
        print(number) # This is for output of 1 - 10
        total = total + number # sum
        count = count + 1      # average

# Calculate for average
average = total / count

# Final output
print(f"\nThe final sum of numbers is {total}")
print(f"The average of numbers is {average:.2f}")

