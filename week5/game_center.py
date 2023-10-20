n_coins = int(input('Enter number of coins: '))

while n_coins > 0:
    game = input('Enter game to play: ')
    price = int(input('Enter price per minute: '))
    play_this_game = True
    while play_this_game:
        minutes = int(input('Enter number of minutes to play: '))
        if price * minutes > n_coins:
            print('Not enough coins to play')
            break

        n_coins -= minutes * price
        print(f'Playing in {minutes} minutes')
        print(f'Current coins: {n_coins}')

        answer = input('Do you want to play again (y/n): ')
        play_this_game = answer == 'y'