# Project #3 + Coding Exercise 1

# Variable declaresg
MAX_TEMP = 102.5
count = 0
summation = 0

# Get the substance's temperature.
temperature = float(input("Enter the temperature in Celsius for today: "))

# As long as necessary, instruct the user to adjust the thermostat.
while temperature < MAX_TEMP:

    summation = summation + temperature
    count = count + 1
    temperature = float(input("Enter new Celsius temperature: "))

# Average
average = summation / count

# Final output
print(f"\nThe sum of {count} temps is {summation}.\nThe average of {count} temps is {average}.")


# Project 4 + Challenge Exercise #2

# This program demonstrates an infinite loop.
# Create a variable to control the loop.
total = 0
keep_going = 'y'

# Warning! Infinite loop!
while keep_going == 'y':
    # Get a sales person's sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    # Calculate the commission.
    commission = sales * comm_rate
    total = total + commission

    # Display the commission.
    print(f"The commission is ${commission:,.2f}.")

    keep_going = input("Keep going? y/n: ")

print(f"The total is ${total:.2f}.")


# Project #5 + Challenge Exercise #3

print('I will display the numbers 1 through 10.')
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: # the numbers are placed in an array
    print(num)

# Project #6 + Challenge Exercise #4

# This program also demonstrates a simple for loop that uses a list of strings.
for name in ['Arambulo Erick']:
    print(f"Your full name is {name}")

# Project #7 + Challenge Exercise #5

# This program demonstrates how the range function can be used with a for loop.
# Print a message five times.
for x in range(10):
    print('Hello world')

# Project #10 + Challenge Exercise #6

# This program calculates the sum of a series of numbers entered by the user.
MAX = 5 # The maximum nunber

# Initialize an accumulator variable.
total = 0.0
count = 0

# Explain what we are doing.
print("This program calculates the sum of")
print(f"{MAX} numbers you will enter.")

# get the numbers and accumulate them.
for counter in range(MAX):
    number = int(input("Enter a number: "))
    total = total + number
    count = count + 1

    print(f"The total is {total}.")

# Average
average = total / count
print(f"The average of the {count} numbers is {average}.")
