from __future__ import division
from ast import Delete
from tkinter import *
from turtle import width

# Sets root as a shortcut to the Tk module
root = Tk()

# Sets the GUI title in the title bar
root.title("Calculator - GUI Training")

# Global variables to be used
first_number = 0
math = ""

def button_click(number):
    # data_entry.delete(0, END)
    if number in range(0, 10):
        data_entry.insert(len(data_entry.get()), number)

def button_clear():
    global btn_state
    data_entry.delete(0, END)
    state_change()

def button_addition():
    # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "addition"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_subtraction():
        # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "subtraction"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_division():
        # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "division"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_multiplication():
    # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "multiplication"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_mod():
    # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "modulo"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_basedivision():
    # Used to access the global variable
    global first_number
    global math

    # Used to set the global variable
    first_number = int(data_entry.get())
    math = "basedivision"

    # Clears the text box for new input
    data_entry.delete(0, END)

def button_process(number, type):
    current_num = data_entry.get()
    data_entry.delete(0, END)
    state_change()
    
    if type == "addition":
        data_entry.insert(0, int(number) + int(current_num))
    
    if type == "subtraction":
        data_entry.insert(0, int(number) - int(current_num))
    
    if type == "division":
        data_entry.insert(0, int(number) / int(current_num))
    
    if type == "multiplication":
        data_entry.insert(0, int(number) * int(current_num))
    
    if type == "modulo":
        data_entry.insert(0, int(number) % int(current_num))
    
    if type == "basedivision":
        data_entry.insert(0, int(number) // int(current_num))

def state_change():
    btn_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9,
        button_0, button_add, button_minus, button_divide, button_multiply, button_modulo, button_basedivide,
        button_equal]
    
    for btn in btn_list:
        if btn['state'] == NORMAL:
            btn["state"] = DISABLED
        else:
            btn["state"] = NORMAL







# Text box for data entry in the calculator application
data_entry = Entry(root, width=40, borderwidth=3)

# Calculator buttons configured to include size and related command
button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command= lambda: button_addition())
button_minus = Button(root, text="-", padx=40, pady=20, command= lambda: button_subtraction())
button_divide = Button(root, text="/", padx=40, pady=20, command= lambda: button_division())
button_multiply = Button(root, text="*", padx=40, pady=20, command= lambda: button_multiplication())
button_modulo = Button(root, text="MOD", padx=28, pady=20, command= lambda: button_mod())
button_basedivide = Button(root, text="//", padx=38, pady=20, command= lambda: button_basedivision())
button_equal = Button(root, text="=", padx=80, pady=20, command= lambda: button_process(first_number, math))
button_clr = Button(root, text="Clear", padx=80, pady=20, command= lambda: button_clear())


# Calculator grid output of the text box and the created buttons
data_entry.grid(row=2, column=0,  columnspan=4, padx= 10, pady= 10)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_add.grid(row=3, column=3)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_minus.grid(row=4, column=3)
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_divide.grid(row=5, column=3)
button_modulo.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_basedivide.grid(row=6, column=2)
button_multiply.grid(row=6, column=3)
button_equal.grid(row=7, column=0, columnspan=2)
button_clr.grid(row=7, column= 2, columnspan=2)


# Operational loop to be used to keep the GUI active and refreshing
root.mainloop()