# Project #1: Automobile Costs

def total_cost():
    # Ask users for their inputs
    loan_payment = float(input("Enter the monthly costs for loan payment: $"))
    insurance = float(input("Enter the monthly costs for insurance: $"))
    gas = float(input("Enter the monthly costs for gas: $"))
    oil = float(input("Enter the monthly costs for oil: $"))
    tires = float(input("Enter the monthly costs for tires: $"))
    maintenance = float(input("Enter the monthly costs for maintenance: $"))

    # Calculations
    # Monthly cost (1 month)
    monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    # Yearly cost (12 months)
    annual_cost = (loan_payment * 12) + (insurance * 12) + (gas * 12) + (oil * 12) + (tires * 12) + (maintenance * 12)
    
    # Final output
    print(f"The monthly cost is ${monthly_cost:.2f}.\nThe annual cost is ${annual_cost:.2f}.")

# Calls function
total_cost()


# Project #2: Monthly Sales Tax

# Function defined
def monthly_sales_tax(total):
    # Variables declared and initialized
    state_sales_tax_rate = 0.05
    county_sales_tax_rate = 0.025

    # Calculations
    amountStateSalesTax = total * state_sales_tax_rate
    amountCountySalesTax = total * county_sales_tax_rate
    total_sales_tax = amountCountySalesTax + amountStateSalesTax

    # Final output
    print(f"\nThe amount of state sales tax is ${amountStateSalesTax:.2f}.")
    print(f"The amount of county sales tax is ${amountCountySalesTax:.2f}.")
    print(f"The amount of total sales tax is ${total_sales_tax:.2f}.")

# Ask users to enter their total sales for the month
userInput = float(input("Please enter the total sales for the month: $"))

# Calls function
monthly_sales_tax(userInput)


# Project #3: Sum of Numbers

# Function defined
def sum_and_average():
    total = 0 # Sum part
    count = 0 # Average part

    # Open the file, numbers.txt
    with open("numbers.txt", "r") as file:
        for line in file: # Note to myself: this enable me to read EACH line
            number = int(line)
            print(number)
            total = total + number
            count = count + 1

    # Find the averagee
    average = total / count
    print(f"\nTotal sum of numbers is {total}")
    print(f"The average of numbers is {average:.2f}")

# Calls function
sum_and_average()


# Project #4: Random Number File Writer

# Import random package
import random

# Ask user for their input based on how many random numbers the file will hold
userInput = int(input("Please enter how many random numbers the file will hold: "))

# Create a file within this program (I think??)
with open("random_generator.txt", "w") as file:
    # for loop
    for x in range(userInput):
        # Random numbers generator
        numbers = random.randint(1, 10)
        
        # Write to file
        file.write(str(numbers) + '\n')

        print(numbers)

        