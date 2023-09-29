product = input('Enter product name: ')
price = int(input('Enter price: '))
quantity = int(input('Enter quantity: '))
payment = price * quantity

header = '-' * 12 + 'Receipt' + '-' * 12
print(header)

print('Product:', f'{product:>21}')
print('Price:', f'{price:>23}')
print('Quantity:', f'{quantity:>20}')

footer = 'Payment: ' + str(payment)
print(f'{footer:^31}')