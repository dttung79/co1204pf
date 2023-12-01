from tkinter import *
from tkinter import messagebox as msb

#### 1. CREATE WINDOW ####
window = Tk()
window.title("Arithmetic Operators")
window.geometry("300x200") # size of window

#### 2. EVENT HANDLER ####
def calculate(operator):
    try:
        a = int(txt_a.get())
        b = int(txt_b.get())
        if operator == '+':
            c = a + b
        elif operator == '-':
            c = a - b
        elif operator == 'x':
            c = a * b
        else:
            c = a / b
        
        txt_c.delete(0, END)
        txt_c.insert(0, c)
    except ValueError:
        msb.showerror('Error', 'Invalid input. Must be numbers.')
    except ZeroDivisionError:
        msb.showerror('Error', 'Cannot divide by zero.')

def btn_add_clicked():
    calculate('+')

def btn_sub_clicked():
    calculate('-')

def btn_mul_clicked():
    calculate('x')

def btn_div_clicked():
    calculate(':')

#### 3. ADD WIDGETS ####
lbl_a = Label(window, text="a = ")
lbl_a.grid(row=0, column=0)

txt_a = Entry(window, width=20)
txt_a.grid(row=0, column=1, columnspan=4)

lbl_b = Label(window, text="b = ")
lbl_b.grid(row=1, column=0)

txt_b = Entry(window, width=20)
txt_b.grid(row=1, column=1, columnspan=4)

lbl_c = Label(window, text="c = ")
lbl_c.grid(row=2, column=0)

txt_c = Entry(window, width=20)
txt_c.grid(row=2, column=1, columnspan=4)

btn_add = Button(window, text="+", width=2, command=btn_add_clicked)
btn_add.grid(row=3, column=1)

btn_sub = Button(window, text="-", width=2, command=btn_sub_clicked)
btn_sub.grid(row=3, column=2)

btn_mul = Button(window, text="x", width=2, command=btn_mul_clicked)
btn_mul.grid(row=3, column=3)

btn_div = Button(window, text=":", width=2, command=btn_div_clicked)
btn_div.grid(row=3, column=4)
#### 4. RUN WINDOW ####
window.mainloop()