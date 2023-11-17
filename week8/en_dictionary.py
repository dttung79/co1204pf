envi_dict = {}

def print_dictionary():
    for en_word, vi_word in envi_dict.items():
        print(f'{en_word}: {vi_word}')
    
def add_word():
    en_word = input('Enter a new English world: ')
    vi_word = input('Enter a translation in Vietnamese: ')
    if en_word in envi_dict:
        print(f'{en_word} is already in the dictionary')
    else:
        envi_dict[en_word] = vi_word
        print(f'Added {en_word} to the dictionary')
        print(envi_dict)

def edit_word():
    en_word = input('Enter a current English word: ')
    vn_word = input('Enter a new Vietnamese translation: ')
    if en_word not in envi_dict:
        print(f'{en_word} is not in the dictionary')
    else:
        envi_dict[en_word] = vn_word
        print(f'Updated {en_word} in the dictionary')
        print(envi_dict)

def delete_word():
    en_word = input('Enter a current English world to delete: ')
    if en_word not in envi_dict:
        print(f'{en_word} is not in the dictionary')
    else:
        envi_dict.pop(en_word)
        print(f'{en_word} is removed.')
        print(envi_dict)

def search_word():
    en_word = input('Enter an English word: ')
    if en_word in envi_dict:
        print(f'{en_word} in Vietnamese is {envi_dict[en_word]}')
    else:
        print(f'{en_word} is not in the dictionary')

def print_menu():
    print('ENGLISH - VIETNAMESE DICTIONARY')
    print('1. Print the dictionary')
    print('2. Add a new word')
    print('3. Edit an existing word')
    print('4. Delete an existing word')
    print('5. Search for a word')
    print('6. Quit')

### main program ###
running = True
while running:
    print_menu()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print_dictionary()
    elif choice == 2:
        add_word()
    elif choice == 3:
        edit_word()
    elif choice == 4:
        delete_word()
    elif choice == 5:
        search_word()
    elif choice == 6:
        running = False
    else:
        print('Invalid choice. Please try again.')