from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('500x300')

books = {'Introduction to Python': ['John Smith', 500, 20.00],
         'Python for Beginners': ['Jane Potter', 600, 25.00],
         'Python for Experts': ['Peter Lando', 300, 30.00],
         'Python for Dummies': ['Paul McCarteney', 250, 35.00],
         'Python for Geeks': ['Mary Lavender', 330, 24.00]}

###### 2. IMPLEMENT HANDLERS ######
def lst_books_selected(event):
    # get selected index
    index = lst_books.curselection()[0]
    book_name = lst_books.get(index)
    book_info = books[book_name] # book_info is a list of 3 elements
    author = book_info[0]
    pages = book_info[1]
    price = book_info[2]
    # display book info in textboxes
    set_text(txt_author, author)
    set_text(txt_pages, pages)
    set_text(txt_price, price)

def set_text(entry, content):
    entry.config(state=NORMAL)      # enable entry to write
    entry.delete(0, END)            # clear entry
    entry.insert(END, content)      # insert content    
    entry.config(state='readonly')  # disable entry to read only

def btn_buy_clicked():
    price = float(txt_price.get())
    shipping = cbb_shipping.get()
    # $1 for Normal, $3 for Express, $5 for Now
    price += 1 if shipping == 'Normal' else 3 if shipping == 'Express' else 5

    if cover_var.get():
        price += 2      # add $2 for cover
    if card_var.get():
        price += 3      # add $3 for greeting card
    
    lbl_payment.config(text=f'Payment: ${price}')
###### 3. CREATE WIDGETS ######
lbl_books = Label(window, text='Books')
lbl_books.grid(row=0, column=0, padx=10, pady=2)

lst_books = Listbox(window, height=12, width=20, selectmode=SINGLE, exportselection=False)
lst_books.grid(row=1, column=0, padx=10, pady=2, rowspan=7)
book_names = list(books.keys())
lst_books.insert(END, *book_names)
lst_books.bind('<<ListboxSelect>>', lst_books_selected)

lbl_author = Label(window, text='Author:')
lbl_author.grid(row=1, column=1, padx=10, pady=2, sticky=W)

txt_author = Entry(window, width=20, state='readonly')
txt_author.grid(row=1, column=2, padx=10, pady=2, sticky=W)

lbl_pages = Label(window, text='Pages:')
lbl_pages.grid(row=2, column=1, padx=10, pady=2, sticky=W)

txt_pages = Entry(window, width=20, state='readonly')
txt_pages.grid(row=2, column=2, padx=10, pady=2, sticky=W)

lbl_price = Label(window, text='Price:')
lbl_price.grid(row=3, column=1, padx=10, pady=2, sticky=W)

txt_price = Entry(window, width=20, state='readonly')
txt_price.grid(row=3, column=2, padx=10, pady=2, sticky=W)

lbl_shipping = Label(window, text='Shipping:')
lbl_shipping.grid(row=4, column=1, padx=10, pady=2, sticky=W)

cbb_shipping = Combobox(window, width=18, state='readonly')
cbb_shipping.grid(row=4, column=2, padx=10, pady=2, sticky=W)
ship_modes = ['Standard', 'Express', 'Now']
cbb_shipping['values'] = ship_modes

lbl_extra = Label(window, text='Extra:')
lbl_extra.grid(row=5, column=1, padx=10, pady=2, sticky=W)

cover_var = BooleanVar()
cb_cover = Checkbutton(window, text='Cover', variable=cover_var)
cb_cover.grid(row=5, column=2, padx=10, pady=2, sticky=W)

card_var = BooleanVar()
cb_card = Checkbutton(window, text='Greeting Card', variable=card_var)
cb_card.grid(row=6, column=2, padx=10, pady=2, sticky=W)

btn_buy = Button(window, text='Buy', width=3,command=btn_buy_clicked)
btn_buy.grid(row=7, column=1, padx=10, pady=2, sticky=W)

lbl_payment = Label(window, text='Payment: $0')
lbl_payment.grid(row=7, column=2, padx=10, pady=2, sticky=W)
###### 4. MAIN LOOP ######
window.mainloop()