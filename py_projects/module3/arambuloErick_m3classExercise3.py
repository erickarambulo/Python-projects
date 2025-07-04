# Project #1: Kilometer Converter

# Function
def kilometer_converter(kilometers):
    miles = kilometers * 0.6214
    print(f"The kilometer(s) you entered is {kilometers}, which converts into {miles:.4f} mile(s).")

# Variable declared
userInput = int(input("Please enter the number of kilometers: "))

# Calls a function
kilometer_converter(userInput)


# Project #2: Automobile Costs

def monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance):
    # Calculation
    total_monthly = loan_payment + insurance + gas + oil + tires + maintenance
    total_annual = (loan_payment * 12) + (insurance * 12) + (gas * 12) + (oil * 12) + (tires * 12) + (maintenance * 12)
    # Final output
    print(f"Your total for monthly cost is ${total_monthly:.2f}, and annual cost is ${total_annual:.2f}.")

# Ask users to input their numbers
loan_payment = float(input("Enter the monthly cost for loan payment: $"))
insurance = float(input("Enter the monthly cost for insurance: $"))
gas = float(input("Enter the monthly cost for gas: $"))
oil = float(input("Enter the monthly cost for oil: $"))
tires = float(input("Enter the monthly cost for tires: $"))
maintenance = float(input("Enter the monthly cost for maintenance: $"))

# Calls a function
monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance)


# Project #3: Property Tax

# Function defined
def property_tax(total):
    # Variables declared
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


# Project #4: Monthly Sales Tax

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

