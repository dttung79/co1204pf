def convert_temparature(temp, unit):
    if unit.lower() == 'c':
        return temp * 9 / 5 + 32
    elif unit.lower() == 'f':
        return (temp - 32) * 5 / 9
    else:
        return None


t = float(input('Enter the temperature: '))
u = input('Enter the unit: ')
convert = convert_temparature(t, u)

if u.lower() == 'c':
    print(f'{t}C = {convert}F')
elif u.lower() == 'f':
    print(f'{t}F = {convert}C')
else:
    print('Invalid unit')