from tkinter import *
from tkinter import messagebox as msb

#### 1. CREATE WINDOW ####
window = Tk()
window.title("Python Question")
window.geometry("300x200") # size of window

#### 2. EVENT HANDLER ####
def btn_check_clicked():
    points = 0
    n_checks = 0

    if op1_var.get() == True:
        points += 5
        n_checks += 1
    
    if op2_var.get() == True:
        n_checks += 1

    if op3_var.get() == True:
        points += 5
        n_checks += 1
    
    if op4_var.get() == True:
        n_checks += 1
    
    if n_checks > 2: # more than 2 options are checked
        points = 0

    lbl_result.config(text=f'Point: {points} pts')
#### 3. ADD WIDGETS ####
lbl_question = Label(window, text='Choose 2 valid Python operators')
lbl_question.grid(row=0, column=0)

op1_var = BooleanVar()
cb_option_1 = Checkbutton(window, text='+=', variable=op1_var)
cb_option_1.grid(row=1, column=0, sticky=W)

op2_var = BooleanVar()
cb_option_2 = Checkbutton(window, text='=+', variable=op2_var)
cb_option_2.grid(row=2, column=0, sticky=W)

op3_var = BooleanVar()
cb_option_3 = Checkbutton(window, text='!=', variable=op3_var)
cb_option_3.grid(row=3, column=0, sticky=W)

op4_var = BooleanVar()
cb_option_4 = Checkbutton(window, text='=!', variable=op4_var)
cb_option_4.grid(row=4, column=0, sticky=W)

btn_check = Button(window, text='Check Answer', command=btn_check_clicked)
btn_check.grid(row=5, column=0, sticky=W)

lbl_result = Label(window, text='Point: 0 pts')
lbl_result.grid(row=6, column=0, sticky=W)
#### 4. RUN WINDOW ####
window.mainloop()