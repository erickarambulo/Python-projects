# Project 1

price = float(input("Enter the original price of the item: "))

# According to the Class Exercise #1, it says it needs to have 2 0's
# after decimal ($80.00, not $80.0)
result = price - round(price * 0.20, 2)
finalResult = f"{result:.2f}"

print("The sale price after a 20% discount is: $" + str(finalResult))


# Project 2

userInputMilesDriven = float(input("Enter the number of miles driven: "))
userInputGas = float(input("Enter the gallons of gas used: "))

mpg = userInputMilesDriven / userInputGas
# Properly convert from 2.0 to 2.00 (with two zeros after decimal)
result = f"{mpg:.2f}"

print("The car's miles-per-gallon (MPG) is: " + str(result))


# Project 3

userInput = float(input("Enter the projected amount of total sales: "))

calculation = userInput * 0.23
# Properly convert from 2.0 to 2.00 (with two zeros after decimal)
result = f"{calculation:.2f}"

print("The projected profit is: $" + str(result))


# Project 4

userInput = float(input("Enter the charge for the food: $"))

# Tip amount is 18%
tipAmount = userInput * 0.18
# Sales tax amount is 7%
salesTaxAmount = userInput * 0.07
# Total amount
totalAmount = userInput + tipAmount + salesTaxAmount

# Properly convert from 2.0 to 2.00 (with two zeros after decimal)
resultTipAmount = f"{tipAmount:.2f}"
resultSalesTaxAmount = f"{salesTaxAmount:.2f}"
resultTotalAmount = f"{totalAmount:.2f}"

# Final output
print("\nTip amount (18%): $" + str(resultTipAmount))
print("Sales tax amount (7%): $" + str(resultSalesTaxAmount))
print("Total amount: $" + str(resultTotalAmount))


# Project 5

# Numbers given
numberShares = 2000
perShare = 40.00
commission = 0.03
perShareWhenSold = 42.75

# Used Google to help me to find the formula that I needed to use
purchasePrice = numberShares * perShare # = 80000
commissionPurchase = purchasePrice * commission # = 2400
profit = (numberShares * perShareWhenSold) - commissionPurchase # (2000 * 42.75) - 2400 = 83100 

# Convert them into .00 (2 0's after a decimal)
finalPurchasePrice = f"{purchasePrice:.2f}"
finalCommissionPurchase = f"{commissionPurchase:.2f}"
finalProfit = f"{profit:.2f}"

# Final output
print("The amount of money Joe paid for the stock is $" + str(finalPurchasePrice))
print("The amount of money Joe paid the broker is $" + str(finalCommissionPurchase))
print("Joe profited $" + str(finalProfit))
