# Project #1: Number Analysis Program

# A simple instruction for users
print("Hello! Please enter a series of 20 numbers:")

# Empty list
numbers = []

# For loop to append numbers to an empty list
for x in range(1, 21):
    # Ask user to input their numbers
    userInput = int(input("Enter your number: "))
    numbers.append(userInput)

max_number = max(numbers)
min_number = min(numbers)

print(f"\nThe min number: {min_number}\nThe max number: {max_number}")

# For loop to find sum and average
total = 0
count = 0
for y in numbers:
    total = total + y
    count = count + 1

# Calculate for average
average = total / count

# Final output
print(f"The total of the numbers in the list: {total}")
print(f"The average of the numbers in the list: {average:.2f}")


# Project #2: Name Search
# Note to myself: Only list 20 names, not 200

# Empty list to add boy names
boyNames = []

# Empty list to add girl names
girlNames = []

# Open the file and transfer the name to boyNames and girlNames lists
with open("BoyNames.txt", "r") as file:
    for line in file:
        boyNames.append(line.strip())  # Used strip to remove whitespace

with open("GirlNames.txt", "r") as file:
    for line in file:
        girlNames.append(line.strip()) # Used strip to remove whitespace

# Ask user for a name to see if it's in both boy and girl lists
userInput = input("Please enter the name to determine if the name is among top 20 names: ")

if userInput.capitalize() in boyNames or userInput.capitalize() in girlNames: # Must be capitalized for names
    print("Your name choice is in the top 20 list!")
else:
    print("Your name choice is not in the top 20 list!")

