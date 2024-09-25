import tkinter as tk
from tkinter import *

# Function to update the input field whenever a button is clicked
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear the input field
def button_clear():
    input_text.set("")

# Function to evaluate the expression in the input field
def button_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

# Create the main window
root = Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# StringVar to store the input
input_text = StringVar()

# Create an entry widget for the display
input_frame = Frame(root)
input_frame.pack(pady=50)

input_field = Entry(input_frame, textvariable=input_text, font=('arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack()

# Create the buttons
buttons_frame = Frame(root)
buttons_frame.pack()

# First row
button_1 = Button(buttons_frame, text='1', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(1))
button_1.grid(row=1, column=0)

button_2 = Button(buttons_frame, text='2', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(2))
button_2.grid(row=1, column=1)

button_3 = Button(buttons_frame, text='3', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(3))
button_3.grid(row=1, column=2)

button_add = Button(buttons_frame, text='+', padx=20, pady=20, font=('arial', 18), command=lambda: button_click('+'))
button_add.grid(row=1, column=3)

# Second row
button_4 = Button(buttons_frame, text='4', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = Button(buttons_frame, text='5', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = Button(buttons_frame, text='6', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_subtract = Button(buttons_frame, text='-', padx=23, pady=20, font=('arial', 18), command=lambda: button_click('-'))
button_subtract.grid(row=2, column=3)

# Third row
button_7 = Button(buttons_frame, text='7', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(7))
button_7.grid(row=3, column=0)

button_8 = Button(buttons_frame, text='8', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(8))
button_8.grid(row=3, column=1)

button_9 = Button(buttons_frame, text='9', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(9))
button_9.grid(row=3, column=2)

button_multiply = Button(buttons_frame, text='*', padx=23, pady=20, font=('arial', 18), command=lambda: button_click('*'))
button_multiply.grid(row=3, column=3)

# Fourth row
button_0 = Button(buttons_frame, text='0', padx=20, pady=20, font=('arial', 18), command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_clear = Button(buttons_frame, text='C', padx=20, pady=20, font=('arial', 18), command=button_clear)
button_clear.grid(row=4, column=1)

button_equal = Button(buttons_frame, text='=', padx=20, pady=20, font=('arial', 18), command=button_equal)
button_equal.grid(row=4, column=2)

button_divide = Button(buttons_frame, text='/', padx=23, pady=20, font=('arial', 18), command=lambda: button_click('/'))
button_divide.grid(row=4, column=3)

# Start the GUI loop
root.mainloop()
