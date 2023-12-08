from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('450x300')

###### 2. IMPLEMENT HANDLERS ######
def calculate_payment(shoes, color, quantity):
    price = 100 if shoes == 'Nike' else 80 if shoes == 'Adidas' else 60
    price += 10 if color == 'Brown' else 20 if color == 'Red' else 0
    payment = price * quantity

    return payment

def shoes_selected(event):
    shoes = cbb_shoes.get()
    color = cbb_color.get()
    quantity = int(cbb_quantity.get())

    payment = calculate_payment(shoes, color, quantity)

    shoes_info = f'Shoes: {shoes} - Color: {color} - Quantity: {quantity}'
    lbl_chosen.config(text=shoes_info)

    payment_info = f'Payment: ${payment}'
    lbl_payment.config(text=payment_info)

###### 3. CREATE WIDGETS ######
lbl_shoes = Label(window, text='Shoes:')
lbl_shoes.grid(row=0, column=0, padx=10, pady=2, sticky=W)

cbb_shoes = Combobox(window, width=10, state='readonly')
cbb_shoes.grid(row=1, column=0, padx=10, pady=2, sticky=W)
cbb_shoes['values'] = ['Nike', 'Adidas', 'Puma']
cbb_shoes.current(0)
cbb_shoes.bind('<<ComboboxSelected>>', shoes_selected)

lbl_color = Label(window, text='Color:')
lbl_color.grid(row=0, column=1, padx=10, pady=2, sticky=W)

cbb_color = Combobox(window, width=10, state='readonly')
cbb_color.grid(row=1, column=1, padx=10, pady=2, sticky=W)
cbb_color['values'] = ['White', 'Brown', 'Red']
cbb_color.current(0)
cbb_color.bind('<<ComboboxSelected>>', shoes_selected)

lbl_quantity = Label(window, text='Quantity:')
lbl_quantity.grid(row=0, column=2, padx=10, pady=2, sticky=W)

cbb_quantity = Combobox(window, width=10, state='readonly')
cbb_quantity.grid(row=1, column=2, padx=10, pady=2, sticky=W)
cbb_quantity['values'] = ['1', '2', '3', '4', '5']
cbb_quantity.current(0)
cbb_quantity.bind('<<ComboboxSelected>>', shoes_selected)

lbl_chosen = Label(window, text='Chosen shoes:')
lbl_chosen.grid(row=2, column=0, padx=10, pady=2, sticky=W, columnspan=3)

lbl_payment = Label(window, text='Payment: $0')
lbl_payment.grid(row=3, column=0, padx=10, pady=2, sticky=W)

###### 4. MAIN LOOP ######
window.mainloop()