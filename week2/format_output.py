s = 'hello world'
a = 10
f = 1.25
# without formating, python use just enough spaces to print the values
print(s)
print(a)
print(f)

# format output
print(f'|{s:20}|') # by default, string is aligned to the left
print(f'|{a:20}|') # by default, number is aligned to the right
print(f'|{f:20}|')

# manually align the output
print(f'|{s:>20}|') # align to the right
print(f'|{a:<20}|') # align to the left
print(f'|{f:^20}|') # align to the center

id = 1
name = 'John'
print(f'|{id:5}|{name:>20}|')
id = 2
name = 'Paul'
print(f'|{id:5}|{name:>20}|')
id = 3
name = 'Marry'
print(f'|{id:5}|{name:>20}|')