from tkinter import *
from tkinter import messagebox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('250x300')

###### 2. IMPLEMENT HANDLERS ######
def lst_students_selected(event):
    # get current slected index
    index = lst_students.curselection()[0]
    # get student name at that index
    name = students[index]
    # display student name in textbox
    txt_selected.delete(0, END)
    txt_selected.insert(END, name)

###### 3. CREATE WIDGETS ######
lbl_students = Label(window, text='Students')
lbl_students.grid(row=0, column=0, padx=10, pady=2)

lst_students = Listbox(window, height=5, width=20, selectmode=SINGLE)
lst_students.grid(row=1, column=0, padx=10, pady=2)
lst_students.bind('<<ListboxSelect>>', lst_students_selected)

students = ['John', 'Mary', 'Peter', 'Jane', 'Paul']
# add students to listbox
lst_students.insert(END, *students)

lbl_selected = Label(window, text='Selected student:')
lbl_selected.grid(row=2, column=0, padx=10, pady=2, sticky=W)

txt_selected = Entry(window, width=20)
txt_selected.grid(row=3, column=0, padx=10, pady=2, sticky=W)

###### 4. MAIN LOOP ######
window.mainloop()