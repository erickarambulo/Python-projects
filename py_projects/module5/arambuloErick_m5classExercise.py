# Challenge Exercise #1: Total Sales App

# Days of week list in tuple
from calendar import week

days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Empty list
sales = []

# For loop
for day in days_of_week:
    # Ask user for an input of sale
    userInput = float(input(f"Enter a store's sales for {day}: $"))
    # Append to list
    sales.append(userInput)

# Since Jason Sim wants us to give an output in tuple instead of list
week_sales = tuple(sales)

# Add sales for 7 days in a week
total = 0
for x in week_sales:
    total = total + x

# Final output
print(f"Total sales this week is ${total:.2f}")

# Write to a file
with open("weekly_sales.txt", "w") as file:
    for y in range(len(days_of_week)):
        file.write(f"{days_of_week[y]}: ${week_sales[y]:.2f}\n")
    file.write(f"Total Sales: ${total:.2f}")


# Challenge Exercise #2: Rainfall App

# Months in tuple
months_of_year = ("January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December")

# Empty list
rainfall_list = []

# For loop
for month in months_of_year:
    # Ask users to input their total rainfall for each month
    userInput = float(input(f"Enter the total rainfall for {month}: "))
    # Append to list
    rainfall_list.append(userInput)

# Convert list into tuple as requested
monthly_rainfall = tuple(rainfall_list)
# Find min and max vlaue
max_value_rainfall = max(monthly_rainfall)
min_value_rainfall = min(monthly_rainfall)

# 12 months in a year total of rainfall
total = 0
count = 0 # Only for average
for x in monthly_rainfall:
    total = total + x
    count = count + 1

# Sum output
print(f"The total of rainfall in a year (12 months): {total:.2f}")
# Calculate for average
average = total / count
# Min and max output
print(f"The max value of rainfall: {max_value_rainfall:.2f}")
print(f"The min value of rainfall: {min_value_rainfall:.2f}")
# Average output
print(f"The average of rainfall: {average:.2f}")

# Write to a file
with open("rainfall_result.txt", "w") as file:
    for y in range(len(months_of_year)):
        file.write(f"{months_of_year[y]}: {monthly_rainfall[y]:.2f}\n")
    file.write(f"Total Rainfall: {total:.2f}\n")
    file.write(f"The max value of rainfall: {max_value_rainfall:.2f}\n")
    file.write(f"The min value of rainfall: {min_value_rainfall:.2f}\n")
    file.write(f"Average Rainfall: {average:.2f}")


# Challenge Exercise #3: Loop 1-100

# Empty list for append
numbers = []

# Add to the list using for loop
for x in range(1, 101):
    numbers.append(x)

# Convert from list to tuple as requested
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# Use for loop to find sum and average
total = 0 # For sum
count = 0 # For average
for y in numbers_tuple:
    total = total + y
    count = count + 1

# Calculate for average
average = total / count

# Final output
print(f"\nThe total sum is {total}\nThe average is {average:.2f}")


# Challenge Exercise #4: Use the list and Range Functions

# Use list and range together
numbers = list(range(1, 101))

# Convert from list to tuple
numbers = tuple(numbers)

# Final Output
print(numbers)

