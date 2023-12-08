from tkinter import *
from tkinter import messagebox as msb

#### 1. CREATE WINDOW ####
window = Tk()
window.title("Geometry Question")
window.geometry("200x180") # size of window

#### 2. EVENT HANDLER ####
def btn_check_clicked():
    if city_var.get() == 1:
        msb.showinfo('Result', 'Correct')
    else:
        msb.showwarning('Result', 'Incorrect')

#### 3. ADD WIDGETS ####
lbl_question = Label(window, text='What is the capital of Vietnam?')
lbl_question.grid(row=0, column=0)

city_var = IntVar()
city_var.set(3)

rd_option_1 = Radiobutton(window, text='Hanoi', value=1, variable=city_var)
rd_option_1.grid(row=1, column=0, sticky=W)

rd_option_2 = Radiobutton(window, text='HCM City', value=2, variable=city_var)
rd_option_2.grid(row=2, column=0, sticky=W)

rd_option_3 = Radiobutton(window, text='Da Nang', value=3, variable=city_var)
rd_option_3.grid(row=3, column=0, sticky=W)

rd_option_4 = Radiobutton(window, text='Can Tho', value=4, variable=city_var)
rd_option_4.grid(row=4, column=0, sticky=W)

btn_check = Button(window, text='Check Answer', command=btn_check_clicked)
btn_check.grid(row=5, column=0, sticky=W)

#### 4. RUN WINDOW ####
window.mainloop()