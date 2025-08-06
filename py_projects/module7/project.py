# Import tkinter
import tkinter as tk
from tkinter import messagebox

# List to store all the student records
student_records = []

# Functions defined
def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def update_listbox():
    student_listbox.delete(0, tk.END)
    for student in student_records:
        student_listbox.insert(tk.END, f"ID: {student[0]} | Name: {student[1]} | Course: {student[2]} | Grade: {student[3]}")

def on_select(event):
    selection = student_listbox.curselection()
    if selection:
        index = selection[0]
        student = student_records[index]
        clear_fields()
        id_entry.insert(0, student[0])
        name_entry.insert(0, student[1])
        course_entry.insert(0, student[2])
        grade_entry.insert(0, student[3])

def add_student():
    details = [id_entry.get(), name_entry.get(), course_entry.get(), grade_entry.get()]
    if all(details):
        student_records.append(details)
        update_listbox()
        clear_fields()
        messagebox.showinfo("Success", "Student added.")
    else:
        messagebox.showerror("Error", "Please fill all fields.")

def update_student():
    selection = student_listbox.curselection()
    if selection:
        index = selection[0]
        details = [id_entry.get(), name_entry.get(), course_entry.get(), grade_entry.get()]
        if all(details):
            student_records[index] = details
            update_listbox()
            clear_fields()
            messagebox.showinfo("Success", "Student updated.")
        else:
            messagebox.showerror("Error", "Please fill all fields.")
    else:
        messagebox.showerror("Error", "Select a student to update.")

def delete_student():
    selection = student_listbox.curselection()
    if selection:
        index = selection[0]
        del student_records[index]
        update_listbox()
        clear_fields()
        messagebox.showinfo("Success", "Student deleted.")
    else:
        messagebox.showerror("Error", "Select a student to delete.")

# Open up the window
root = tk.Tk()

# Show input boxes
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

tk.Label(input_frame, text="ID:").grid(row=0, column=0)
id_entry = tk.Entry(input_frame, width=30)
id_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Course:").grid(row=2, column=0)
course_entry = tk.Entry(input_frame, width=30)
course_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Grade:").grid(row=3, column=0)
grade_entry = tk.Entry(input_frame, width=30)
grade_entry.grid(row=3, column=1)

# Buttons
button_frame = tk.Frame(root, padx=10, pady=10)
button_frame.pack()

tk.Button(button_frame, text="Add", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields).grid(row=0, column=3, padx=5)

# Display student list
display_frame = tk.Frame(root, padx=10, pady=10)
display_frame.pack()

tk.Label(display_frame, text="Student Records").pack()

student_listbox = tk.Listbox(display_frame, width=50, height=10)
student_listbox.pack()
student_listbox.bind('<<ListboxSelect>>', on_select)

# Run the program
root.mainloop()