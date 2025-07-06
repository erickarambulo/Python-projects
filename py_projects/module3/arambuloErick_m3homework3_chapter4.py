# Project #1: Distance Traveled

# Ask users to input their number
userInputMph = int(input("What is the speed of the vehicle in mph? "))
userInputHours = int(input("How many hours has it traveled? "))

# Header format?
print("\nHour    Distance Traveled")
print("----    -----------------")

# For loop
for x in range(1, userInputHours + 1):
    distance = x * userInputMph
    print(f"{x}       {distance}")


# Project #2: Average Rainfall

# Variables declared and initialized
total_months = 0
total_rainfall = 0.0

# Ask users to input their number
userInputYears = int(input("Enter the number of years: "))

# Outer loop
for year in range(1, userInputYears + 1):
    # Inner loop
    for month in range(1, 13):
        inches = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
        
        total_months = total_months + 1
        total_rainfall += inches

# Calculate
average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month for the entire period: {average_rainfall:.2f}")


# Project #3: Sum of Numbers

# Variable declared and intialized
addition = 0

# Before starting while loop
print("Note: If you enter a negative number, it'll signal the end of the series.")

# Get user's input to begin while loop
userInput = int(input("Please enter a series of positive numbers: "))

# While loop starts here
while userInput > 0:
    addition = addition + userInput
    userInput = int(input("Please enter a series of positive numbers: "))

print(addition)



