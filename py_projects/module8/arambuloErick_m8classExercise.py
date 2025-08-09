import tkinter as tk
import sqlite3

# Create a tkinter window
window = tk.Tk()
window.title("Customer Information")

# Function to insert data into the SQLite database
def insert_data():
    # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("customer.db")
        c = conn.cursor()

        # Create a table named "customers" if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS customers (name TEXT,
                    age INTEGER,
                    address TEXT,
                    city TEXT,
                    state TEXT,
                    zipcode TEXT)''')

        # Insert data into the "customers" table
        name = entry_name.get()
        age = entry_age.get()
        address = entry_address.get()
        city = entry_city.get()
        state = entry_state.get()
        zipcode = entry_zipcode.get()

        c.execute("INSERT INTO customers (name, age, address, city, state, zipcode) VALUES (?, ?, ?, ?, ?, ?)",
                  (name, age, address, city, state, zipcode))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Clear the entry fields
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_city.delete(0, tk.END)
        entry_state.delete(0, tk.END)
        entry_zipcode.delete(0, tk.END)

# Create labels and entry fields for name, age, address, city, state, and zipcode
label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(window, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_address = tk.Label(window, text="Address:")
label_address.grid(row=2, column=0, padx=10, pady=10)
entry_address = tk.Entry(window)
entry_address.grid(row=2, column=1, padx=10, pady=10)

label_city = tk.Label(window, text="City:")
label_city.grid(row=3, column=0, padx=10, pady=10)
entry_city = tk.Entry(window)
entry_city.grid(row=3, column=1, padx=10, pady=10)

label_state = tk.Label(window, text="State:")
label_state.grid(row=4, column=0, padx=10, pady=10)
entry_state = tk.Entry(window)
entry_state.grid(row=4, column=1, padx=10, pady=10)

label_zipcode = tk.Label(window, text="Zipcode:")
label_zipcode.grid(row=5, column=0, padx=10, pady=10)
entry_zipcode = tk.Entry(window)
entry_zipcode.grid(row=5, column=1, padx=10, pady=10)

# Create a button to insert data into the database
button_insert = tk.Button(window, text = "Insert Data", command=insert_data)
button_insert.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the tkinter event loop
window.mainloop()

