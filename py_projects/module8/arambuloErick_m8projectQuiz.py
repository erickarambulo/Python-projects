import tkinter as tk
import sqlite3
from tkinter import messagebox

# Create a tkinter window
window = tk.Tk()
window.title("Hospital Patient Registration")

# Dropdown for gender
gender_option = ["Male", "Female", "Other"]
selected_gender = tk.StringVar(window)
selected_gender.set(gender_option[0])

# Function to insert data into the SQLite database
def insert_data():
    # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("hospital.db")
        c = conn.cursor()

        # Create a table named "patients" if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS patients (
            full_name TEXT,
            date_of_birth TEXT,
            gender TEXT,
            contact_number TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            emergency_name TEXT,
            emergency_phone TEXT)''')

        # Insert data into the "patients" table
        full_name = entry_full_name.get()
        date_of_birth = entry_date_of_birth.get()
        gender = selected_gender.get()
        contact_number = entry_contact_number.get()
        address = entry_address.get()
        city = entry_city.get()
        state = entry_state.get()
        zip_code = entry_zip_code.get()
        emergency_name = entry_emergency_name.get()
        emergency_phone = entry_emergency_phone.get()

        c.execute("INSERT INTO patients (full_name, date_of_birth, gender, contact_number, address, city, state, zip_code, emergency_name, emergency_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (full_name, date_of_birth, gender, contact_number, address, city, state, zip_code,
                   emergency_name, emergency_phone))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Clear the entry fields
        entry_full_name.delete(0, tk.END)
        entry_date_of_birth.delete(0, tk.END)
        selected_gender.set(gender_option[0])
        entry_contact_number.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_city.delete(0, tk.END)
        entry_state.delete(0, tk.END)
        entry_zip_code.delete(0, tk.END)
        entry_emergency_name.delete(0, tk.END)
        entry_emergency_phone.delete(0, tk.END)

        messagebox.showinfo("Success", "Patient registered successfully!")

# Create labels and entry fields for name, age, address, city, state, and zipcode
label_full_name = tk.Label(window, text="Name:")
label_full_name.grid(row=0, column=0, padx=10, pady=10)
entry_full_name = tk.Entry(window)
entry_full_name.grid(row=0, column=1, padx=10, pady=10)

label_date_of_birth = tk.Label(window, text="Date of Birth (format: DD/MM/YYYY):")
label_date_of_birth.grid(row=1, column=0, padx=10, pady=10)
entry_date_of_birth = tk.Entry(window)
entry_date_of_birth.grid(row=1, column=1, padx=10, pady=10)

# This one is different because Jason Sim is asking me to use dropdown for gender
label_gender = tk.Label(window, text="Gender:")
label_gender.grid(row=2, column=0, padx=10, pady=10)
gender_dropdown = tk.OptionMenu(window, selected_gender, *gender_option)
gender_dropdown.grid(row=2, column=1, padx=10, pady=10)

label_contact_number = tk.Label(window, text="Contact Number:")
label_contact_number.grid(row=3, column=0, padx=10, pady=10)
entry_contact_number = tk.Entry(window)
entry_contact_number.grid(row=3, column=1, padx=10, pady=10)

label_address = tk.Label(window, text="Address:")
label_address.grid(row=4, column=0, padx=10, pady=10)
entry_address = tk.Entry(window)
entry_address.grid(row=4, column=1, padx=10, pady=10)

label_city = tk.Label(window, text="City:")
label_city.grid(row=5, column=0, padx=10, pady=10)
entry_city = tk.Entry(window)
entry_city.grid(row=5, column=1, padx=10, pady=10)

label_state = tk.Label(window, text="State:")
label_state.grid(row=6, column=0, padx=10, pady=10)
entry_state = tk.Entry(window)
entry_state.grid(row=6, column=1, padx=10, pady=10)

label_zip_code = tk.Label(window, text="Zipcode:")
label_zip_code.grid(row=7, column=0, padx=10, pady=10)
entry_zip_code = tk.Entry(window)
entry_zip_code.grid(row=7, column=1, padx=10, pady=10)

label_emergency_name = tk.Label(window, text="Emergency Contact Name:")
label_emergency_name.grid(row=8, column=0, padx=10, pady=10)
entry_emergency_name = tk.Entry(window)
entry_emergency_name.grid(row=8, column=1, padx=10, pady=10)

label_emergency_phone = tk.Label(window, text="Emergency Contact Phone:")
label_emergency_phone.grid(row=9, column=0, padx=10, pady=10)
entry_emergency_phone = tk.Entry(window)
entry_emergency_phone.grid(row=9, column=1, padx=10, pady=10)

# Create a button to insert data into the database
button_insert = tk.Button(window, text = "Submit", command=insert_data)
button_insert.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Start the tkinter event loop
window.mainloop()


