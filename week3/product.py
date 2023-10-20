# input data
customer = input('Enter customer name: ')
product = input('Enter product name: ')
price = int(input('Enter product price: '))
quantity = int(input('Enter amount: '))

total = price * quantity

if total >= 200:
    bonus = 'You got 10% discount'
    total *= 0.9 # total = total * 0.9
elif total >= 100:
    bonus = 'You got freeship and a coupon'
elif total >= 50:
    bonus = 'You got freeship'
else:
    bonus = 'No bonus'

print('------ RECEIPT ------')
print(f'Customer : {customer:>10}')
print(f'Product  : {product:>10}')
print(f'Price    : {price:>10}')
print(f'Quantity : {quantity:>10}')
print(f'Payment  : {total:>10.2f}')
print(f'Bonus    : {bonus}')