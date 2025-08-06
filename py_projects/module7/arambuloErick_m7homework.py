# Project #1

# Import tkinter
import tkinter as tk
from tkinter import messagebox

# Functions defined
def calculate_tax():
    actual_value_str = value_entry.get()
    
    if not actual_value_str:
        messagebox.showerror("Invalid Input!", "Please enter the value")
        return
    
    if not actual_value_str.isdigit():
        messagebox.showerror("Invalid Input!", "Please enter the whole number")
        return

    actual_value = float(actual_value_str)
    assessed_value = actual_value * 0.60
    property_tax = (assessed_value / 100) * 0.75
    
    assessed_value_text = f"${assessed_value:,.2f}"
    property_tax_text = f"${property_tax:,.2f}"
    
    assessed_label.config(text=f"Assessed Value: {assessed_value_text}")
    tax_label.config(text=f"Property Tax: {property_tax_text}")

def clear_fields():
    value_entry.delete(0, tk.END)
    assessed_label.config(text="Assessed Value: ")
    tax_label.config(text="Property Tax: ")

# Starts the root here
root = tk.Tk()

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Actual Property Value:").pack(side=tk.LEFT, padx=5)
value_entry = tk.Entry(input_frame, width=20)
value_entry.pack(side=tk.LEFT)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_tax)
calculate_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

assessed_label = tk.Label(output_frame, text="Assessed Value: ")
assessed_label.pack()

tax_label = tk.Label(output_frame, text="Property Tax: ")
tax_label.pack()

root.mainloop()

# Project #2:

# Import tkinter
import tkinter as tk
from tkinter import messagebox

# A dictionary to store the rates for each category
RATES = {
    "Daytime": 0.07,
    "Evening": 0.12,
    "Off-Peak": 0.05
}

# Function defined
def calculate_charge():
    minutes_str = minutes_entry.get()

    if not minutes_str.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a whole number for minutes.")
        return

    minutes = int(minutes_str)
    
    selected_category = rate_category.get()
    rate = RATES[selected_category]
    
    total_charge = minutes * rate
    
    messagebox.showinfo(
        "Call Charge",
        f"Rate Category: {selected_category}\n"
        f"Minutes: {minutes}\n"
        f"Total Charge: ${total_charge:.2f}"
    )

# start up 
root = tk.Tk()

rate_category = tk.StringVar(value="Daytime")

radio_frame = tk.Frame(root, padx=10, pady=10)
radio_frame.pack(pady=10)

tk.Label(radio_frame, text="Select Rate Category:").pack()

# Each category
tk.Radiobutton(radio_frame, text="Daytime (6:00 A.M. - 5:59 P.M.)", variable=rate_category, value="Daytime").pack(anchor=tk.W)
tk.Radiobutton(radio_frame, text="Evening (6:00 P.M. - 11:59 P.M.)", variable=rate_category, value="Evening").pack(anchor=tk.W)
tk.Radiobutton(radio_frame, text="Off-Peak (midnight - 5:59 A.M.)", variable=rate_category, value="Off-Peak").pack(anchor=tk.W)

minutes_frame = tk.Frame(root, padx=10, pady=10)
minutes_frame.pack()

tk.Label(minutes_frame, text="Enter Minutes of the call:").pack(side=tk.LEFT)
minutes_entry = tk.Entry(minutes_frame, width=15)
minutes_entry.pack(side=tk.LEFT)

# Button for calculate
calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.pack(pady=10)

# Run the program
root.mainloop()
