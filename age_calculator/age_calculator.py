import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age_in_years():
    try:
        birth_date = get_birth_date()
        current_date = datetime.now()
        years = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            years -= 1  # Adjust if the current month/day hasn't reached the birthdate

        result_label.config(text=f"You are {years} years old.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred.")

def calculate_age_in_months():
    try:
        birth_date = get_birth_date()
        current_date = datetime.now()
        months = (current_date.year - birth_date.year) * 12 + (current_date.month - birth_date.month)
        if current_date.day < birth_date.day:
            months -= 1  # Adjust if the current day hasn't reached the birthdate day

        result_label.config(text=f"You have lived approximately {months} months.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred.")

def calculate_age_in_days():
    try:
        birth_date = get_birth_date()
        current_date = datetime.now()
        delta = current_date - birth_date
        days = delta.days

        result_label.config(text=f"You have lived approximately {days} days.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred.")

def get_birth_date():
    birth_year = int(year_entry.get())
    birth_month = int(month_entry.get())
    birth_day = int(day_entry.get())
    birth_date = datetime(birth_year, birth_month, birth_day)

    if birth_date > datetime.now():
        raise ValueError("Birthdate cannot be in the future.")
    return birth_date

# Create the main Tkinter window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Styling
heading_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 12)
result_font = ("Arial", 12, "italic")

# Create and place widgets
heading_label = tk.Label(root, text="Age Calculator", font=heading_font)
heading_label.pack(pady=10)

instructions_label = tk.Label(root, text="Enter your date of birth:", font=label_font)
instructions_label.pack(pady=5)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Year:", font=label_font).grid(row=0, column=0, padx=5, pady=5, sticky="e")
year_entry = tk.Entry(input_frame, width=10, font=label_font)
year_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Month:", font=label_font).grid(row=1, column=0, padx=5, pady=5, sticky="e")
month_entry = tk.Entry(input_frame, width=10, font=label_font)
month_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Day:", font=label_font).grid(row=2, column=0, padx=5, pady=5, sticky="e")
day_entry = tk.Entry(input_frame, width=10, font=label_font)
day_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons for choosing calculation type
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

years_button = tk.Button(button_frame, text="Years Lived", font=button_font, bg="#2196F3", fg="white", command=calculate_age_in_years)
years_button.grid(row=0, column=0, padx=10, pady=5)

months_button = tk.Button(button_frame, text="Months Lived", font=button_font, bg="#4CAF50", fg="white", command=calculate_age_in_months)
months_button.grid(row=0, column=1, padx=10, pady=5)

days_button = tk.Button(button_frame, text="Days Lived", font=button_font, bg="#FF5722", fg="white", command=calculate_age_in_days)
days_button.grid(row=0, column=2, padx=10, pady=5)

# Result label
result_label = tk.Label(root, text="", font=result_font, wraplength=350, justify="center")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
