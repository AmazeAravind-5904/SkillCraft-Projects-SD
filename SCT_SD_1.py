import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()
        
        if unit_from == unit_to:
            result.set(f"{temp:.2f} {unit_to}")
        else:
            if unit_from == "Celsius":
                if unit_to == "Fahrenheit":
                    result.set(f"{celsius_to_fahrenheit(temp):.2f} {unit_to}")
                elif unit_to == "Kelvin":
                    result.set(f"{celsius_to_kelvin(temp):.2f} {unit_to}")
            elif unit_from == "Fahrenheit":
                if unit_to == "Celsius":
                    result.set(f"{fahrenheit_to_celsius(temp):.2f} {unit_to}")
                elif unit_to == "Kelvin":
                    result.set(f"{fahrenheit_to_kelvin(temp):.2f} {unit_to}")
            elif unit_from == "Kelvin":
                if unit_to == "Celsius":
                    result.set(f"{kelvin_to_celsius(temp):.2f} {unit_to}")
                elif unit_to == "Fahrenheit":
                    result.set(f"{kelvin_to_fahrenheit(temp):.2f} {unit_to}")
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Temperature Conversion")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

entry_temp = ttk.Entry(frame, width=10)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

combo_from = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=10)
combo_from.grid(row=0, column=2, padx=5, pady=5)
combo_from.current(0)

combo_to = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=10)
combo_to.grid(row=0, column=3, padx=5, pady=5)
combo_to.current(1)

ttk.Button(frame, text="Convert", command=convert_temperature).grid(row=0, column=4, padx=5, pady=5)

result = tk.StringVar()
ttk.Label(frame, textvariable=result, width=20).grid(row=1, column=0, columnspan=5, pady=10)

root.mainloop()
