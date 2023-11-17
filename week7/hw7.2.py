customers = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Mike', 'John']
tickets = [15, 23, 7, 12, 6, 10, 20]

def find_customer(name):
    for i in range(len(customers)):
        if customers[i] == name:
            return i
    return None

def find_richest_customer():
    max_tickets = tickets[0]
    max_index = 0
    for i in range(len(tickets)):
        if tickets[i] > max_tickets:
            max_tickets = tickets[i]
            max_index = i
    
    return max_index

def avg_tickets():
    s = 0
    for i in range(len(tickets)):
        s += tickets[i]
    
    return s / len(tickets)

def print_above_customers():
    avg = avg_tickets()
    print(f'Average tickets: {avg}')

    for i in range(len(tickets)):
        if tickets[i] > avg:
            print(f'Customer {customers[i]} bought {tickets[i]} tickets')
        
### MAIN ###
running = True
while running:
    print('1. Find customer')
    print('2. Find customer who bought the most tickets')
    print('3. Find customers who bought more than average tickets')
    print('4. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        name = input('Enter customer name: ')
        index = find_customer(name)
        if index == None:
            print(f'Customer {name} not found')
        else:
            print(f'Customer {name} bought {tickets[index]} tickets')
    elif choice == 2:
        max_index = find_richest_customer()
        print(f'Customer {customers[max_index]} bought the most tickets ({tickets[max_index]})')
    elif choice == 3:
        print_above_customers()
    elif choice == 4:
        print('Goodbye')
        running = False
    else:
        print('Invalid choice!')