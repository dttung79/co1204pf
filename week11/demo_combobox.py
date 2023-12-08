from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('250x300')

###### 2. IMPLEMENT HANDLERS ######
def cbb_selected(event):
    # Get the selected color
    color = cbb_background.get()
    # Change the background color of the window
    window.config(bg=color)

###### 3. CREATE WIDGETS ######
lbl_background = Label(window, text='Choose colour:')
lbl_background.grid(row=0, column=0, padx=10, pady=10)

cbb_background = Combobox(window, width=10, state='readonly')
cbb_background.grid(row=1, column=0, padx=10, pady=10)

# Add items to the combobox
cbb_background['values'] = ('red', 'green', 'blue', 'yellow', 'pink')
# Set the default value is the 1st item
cbb_background.current(0)
# Bind selected event to the combobox
cbb_background.bind('<<ComboboxSelected>>', cbb_selected)
###### 4. MAIN LOOP ######
window.mainloop()