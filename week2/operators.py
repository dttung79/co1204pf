# number operators: +, -, *, /, //, %, **
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print('Area of the triangle:', s)




# print('a + b =', a + b)
# print('a - b =', a - b)
# print('a * b =', a * b)
# print('a / b =', a / b)
# print('a // b =', a // b)
# print('a % b =', a % b)
# print('a ** b =', a ** b)
