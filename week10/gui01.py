from tkinter import *
from tkinter import messagebox as msb
# create a window
window = Tk()
window.title("GUI 01")
window.geometry("300x200") # size of window

# event handler
def btn_ok_clicked():
    # get the text from the text box
    name = txt_name.get()
    # show a message box
    msb.showinfo('Hello message', 'Hello ' + name)

# add a label
lbl_name = Label(window, text="Name:")
# place the label in the window
lbl_name.grid(row=0, column=0)

# add a text box
txt_name = Entry(window, width=20)
txt_name.grid(row=0, column=1)

# add a button
btn_ok = Button(window, text="OK", command=btn_ok_clicked)
btn_ok.grid(row=0, column=2)

# run window
window.mainloop()