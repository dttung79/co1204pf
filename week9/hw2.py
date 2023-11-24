products = ['pen', 'pencil', 'eraser', 'ruler', 'notebook']
prices = [100, 50, 30, 150, 200]

def add_product():
    product = input('Enter product name: ')
    price = int(input('Enter product price: '))
    if product in products:
        print('Product already exists!')
        return
    
    products.append(product)
    prices.append(price)

    print(f'Product {product} added successfully!')

def edit_price():
    product = input('Enter product name: ')
    price = int(input('Enter product price: '))

    #pos_found = products.index(product)
    
    pos_found = -1
    for i in range(len(products)):
        if products[i] == product:
            pos_found = i
            break
    
    if pos_found == -1:
        print(f'Product {product} not found!')
        return
    
    prices[pos_found] = price

def delete_product():
    product = input('Enter product name: ')
    if product not in products:
        print(f'Product {product} not found!')
        return
    

    pos_found = products.index(product)
    del products[pos_found]
    del prices[pos_found]

def show_products():
    for i in range(len(products)):
        print(f'{i+1}. {products[i]}: {prices[i]}')

def search_product():
    product = input('Enter product name to search: ')
    # if product not in products:
    #     print(f'Product {product} not found!')
    #     return
    # pos_found = products.index(product)

    pos_found = -1
    for i in range(len(products)):
        if products[i] == product:
            pos_found = i
            break
    if pos_found == -1:
        print(f'Product {product} not found!')
    else:
        print(f'Product {product} ${prices[pos_found]}')

    print(f'Product {product}: ${prices[pos_found]}')

def print_menu():
    print('PRODUCT MANAGEMENT')
    print('1. Add product')
    print('2. Edit product price')
    print('3. Delete product')
    print('4. Show products')
    print('5. Search')
    print('6. Quit')

def main():
    running = True

    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_product()
        elif choice == 2:
            edit_price()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            show_products()
        elif choice == 5:
            search_product()
        elif choice == 6:
            running = False
        else:
            print('Invalid choice!')

### MAIN PROGRAM ###
main()