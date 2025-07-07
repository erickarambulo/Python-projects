# Project #1: Property Tax

# Function defined
def property_tax(total):
    # Variable declared
    percent = 0.60
    tax_rate_per_100 = 0.72

    # Calculation
    assessment = total * percent
    acre_assessed = (assessment / 100) * tax_rate_per_100

    # Final output
    print(f"The assessment value is ${assessment:.2f}.")
    print(f"The tax for the acre assessed at ${assessment:.2f} will be ${acre_assessed:.2f}.")

# Variables declared
userInput = float(input("Please enter the actual value of a piece of property: $"))

# Calls function
property_tax(userInput)


# Project #2: Stadium Seating

# Function defined
def seating_categories(classA, classB, classC):
    # Simple Calculation of total profit
    profit = (classA * 20) + (classB * 15) + (classC * 10)

    # Final output
    print(f"Each class of seats ticket sold:\nClass A: {classA}\nClass B: {classB}\nClass C: {classC}")
    print(f"Amount of income generated from ticket sales is ${profit:.2f}.")


# Variables declared
userInputClassA = int(input("Please enter how many tickets for Class A seats were sold: "))
userInputClassB = int(input("Please enter how many tickets for Class B seats were sold: "))
userInputClassC = int(input("Please enter how many tickets for Class C seats were sold: "))


# Calls function
seating_categories(userInputClassA, userInputClassB, userInputClassC)

# Project #3: Monthly Sales Tax

# Function defined
def monthly_sales_tax(total):
    # Variables declared
    state_sales_tax_rate = 0.05
    county_sales_tax_rate = 0.025

    # Calculation
    amount_of_state_tax = total * state_sales_tax_rate
    amount_of_county_tax = total * county_sales_tax_rate
    combined = amount_of_state_tax + amount_of_county_tax

    # Final output
    print(f"The amount of state tax is ${amount_of_state_tax:.2f} and county tax is ${amount_of_county_tax:.2f}.")
    print(f"The total sales tax is ${combined:.2f}.")

# Ask user to enter their total sales for the month
userInput = float(input("Please enter your total sales for the month: $"))

# Calls function
monthly_sales_tax(userInput)