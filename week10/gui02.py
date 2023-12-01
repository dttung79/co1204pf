from tkinter import *
from tkinter import messagebox as msb

#### 1. CREATE WINDOW ####
window = Tk()
window.title("GUI 02")
window.geometry("300x200") # size of window

#### 2. EVENT HANDLER ####
def btn_buy_clicked():
    # get the price
    price = int(txt_price.get())
    quantity = int(txt_quantity.get())
    payment = price * quantity

    # set the text of lbl_money
    lbl_money.config(text=f'${payment}')

#### 3. ADD WIDGETS ####
lbl_product = Label(window, text="Product:")
lbl_product.grid(row=0, column=0)

lbl_laptop = Label(window, text="Laptop")
lbl_laptop.grid(row=0, column=1, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=1, column=0, sticky=W)

txt_price = Entry(window, width=20)
txt_price.grid(row=1, column=1)

lbl_quantity = Label(window, text="Quantity:")
lbl_quantity.grid(row=2, column=0)

txt_quantity = Entry(window, width=20)
txt_quantity.grid(row=2, column=1)

btn_buy = Button(window, text="Buy", width=18, command=btn_buy_clicked)
btn_buy.grid(row=3, column=1)

lbl_payment = Label(window, text="Payment:")
lbl_payment.grid(row=4, column=0)

lbl_money = Label(window, text="$0")
lbl_money.grid(row=4, column=1, sticky=W)



#### 4. RUN WINDOW ####
window.mainloop()