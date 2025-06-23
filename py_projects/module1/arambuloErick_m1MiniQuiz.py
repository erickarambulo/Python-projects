# Project #1
# Write a program that asks for the hours worked and pay rate for two people, then
# calculates and displays their average pay.

personHour1 = float(input("First person, please enter your weekly hours worked: "))
personPayRate1 = float(input("Please enter your pay rate: "))
personHour2 = float(input("Second person, please enter your weekly hours worked: "))
personPayRate2 = float(input("Please enter your pay rate: "))

calculation = ((personHour1 * personPayRate1) + (personHour2 * personPayRate2))
average_pay = calculation / 2

# Fix the format, from 1 0's to 2 0's 
average = f"{average_pay:.2f}"

# Final output
print("The average pay of two people are $" + str(average))

# Project #2
# Write a program that asks the user for their first name, last name, address, city,
# state, and zip code, then displays the information.

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
address = input("Please enter your address: ")
city = input("Please enter your city: ")
state = input("Please enter your state abbreviation: ")
zipcode = input("Please enter your zipcode: ")

# Final output
print("\nHello " + firstName + " " + lastName + "! Your home address is:\n" +
      address + "\n" + city + ", " + state + " " + zipcode)

# Project 3
# Write a program that asks for a user's salary and bonus,
# then calculate and display the total income

userSalary = float(input("Please enter your salary: $"))
userBonus = float(input("Please enter your bonus: $"))

# Calculation
calculation = userSalary + userBonus
# Convert to 2 0's instead of 1 0's
result = f"{calculation:.2f}"

# Final output
print("Your total income is $" + str(result))


