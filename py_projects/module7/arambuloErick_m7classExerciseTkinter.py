# Project #1

# Import tkinter
import tkinter as tk
from tkinter import messagebox

def average():
    # Must use try and except for credit I guess...
    try:
        fullName = name_entry.get()
        midterm = float(midterm_entry.get())
        final = float(final_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the grades.")
        return

    # Must stay between 0 - 100
    if (midterm < 0 or midterm > 100) or (final < 0 or final > 100):
        messagebox.showerror("Invalid Input", "Please enter grades between 0 and 100.")
        return

    # Calculation for average
    average_grade = (midterm + final) / 2
        
    # if, elif, and else branches for letter grade
    if average_grade >= 90:
        letter_grade = "A"
    elif average_grade >= 80:
        letter_grade = "B"
    elif average_grade >= 70:
        letter_grade = "C"
    elif average_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Display
    result = (
        f"Student Full Name: {fullName}\n"
        f"Midterm Grade: {midterm}\n"
        f"Final Grade: {final}\n"
        f"Average Grade: {average_grade:.2f}\n"
        f"Letter Grade: {letter_grade}\n"
    )

    # Final output 
    messagebox.showinfo("Result", result)

# Create the root window
root = tk.Tk()
root.geometry("300x300")

# Create the label and entry box for students
name_label = tk.Label(root, text="Full name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Create the label and entry box for midterm
midterm_label = tk.Label(root, text="Midterm grade:")
midterm_label.pack(pady=5)
midterm_entry = tk.Entry(root)
midterm_entry.pack(pady=5)

# Create the label and entry box for final term
final_label = tk.Label(root, text="Final grade:")
final_label.pack(pady=5)
final_entry = tk.Entry(root)
final_entry.pack(pady=5)

# submit button
submit_button = tk.Button(root, text="Submit", command=average)
submit_button.pack(pady=10)

# Run program
root.mainloop()


# Project #2

# Import tkinter
from tkinter import *

# Create the root window
root = Tk()
root.geometry('180x200')

# Create a listbox
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

# Inserting the listbox items
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")

# Function for printing the selected listbox value(s)
def selected_item():
    # Traverse the tuple returned by curselection method and print
    # corresponding value(s) in the listbox
    for i in listbox.curselection():
        print(listbox.get(i))

# Create a button widget and map the command para mter to
# selected_item function
btn = Button(root, text='Print Selected', command=selected_item)

# Placing the button and listbox
btn.pack(side="bottom")
listbox.pack()

root.mainloop()


# Project #3

# Import tkinter
import tkinter as tk
from tkinter import messagebox

def gasMileage():
    miles = float(miles_entry.get())
    gallons = float(gallon_entry.get())

    # Calculation for average
    mpg = miles / gallons
    mpg = f"{mpg:.2f}"

    # Display
    result = f"The mpg (miles per gallon) will be {mpg}"

    # Final output 
    messagebox.showinfo("Result", result)

# Create the root window
root = tk.Tk()
root.geometry("300x300")

# Create the label and entry box for gallons
gallon_label = tk.Label(root, text="Enter the number of gallons of gas the car holds:")
gallon_label.pack(pady=5)
gallon_entry = tk.Entry(root)
gallon_entry.pack(pady=5)

# Create the label and entry box for miles
miles_label = tk.Label(root, text="Enter the number of miles it can be driven on a full tank:")
miles_label.pack(pady=5)
miles_entry = tk.Entry(root)
miles_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=gasMileage)
calculate_button.pack(pady=10)

# Run program
root.mainloop()


# Project #4

import tkinter as tk

# Provide services and prices in dictionaryy
services = {
    "Oil change": 30.00,
    "Lube job": 20.00,
    "Radiator flush": 40.00,
    "Transmission flush": 100.00,
    "Inspection": 35.00,
    "Muffler replacement": 200.00,
    "Tire rotation": 20.00
}

service_vars = {}

# Copied from Chegg because I really don't understand how to solve this :( Sorry Jason Sim
# if you're reading this
def update_total():
    """Calculates the new total cost and updates the label."""
    total = sum(services[s] for s, var in service_vars.items() if var.get())
    total_label.config(text=f"Total Charges: ${total:.2f}")

# Create the root window
root = tk.Tk()

# Create a variable for each service and a checkbutton
for service, price in services.items():
    # 1. Create a variable for the checkbox to track its state (on/off)
    var = tk.BooleanVar()
    service_vars[service] = var

    # 2. Create the checkbutton widget
    checkbutton = tk.Checkbutton(
        root,
        text=f"{service}: ${price:.2f}",
        variable=var,
        command=update_total
    )
    
    # 3. Add the checkbutton to the window
    checkbutton.pack(anchor="w")

# Create the label that will display the total
total_label = tk.Label(root, text="Total Charges: $0.00")
total_label.pack(pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
