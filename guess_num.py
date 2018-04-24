#!--codding-utf-8

import random

    
def game(secret):
    guess = 0
    print('---------猜数字游戏！---------')
    secret = random.randint(1,100)
    while guess !=secret:
        # print('---------猜数字游戏！---------')
        tem = input("I'm thinking of a number! Try to guess the number I'm thinking of:")
        guess = int(tem)
        if guess > secret:
            print('Too hign! Guess again:')
        else:
            print('Too low! Guess again:')
    if guess == secret:
        str = input("That's it! Would you like to play again?(yes/no)")
        while str == 'yes':
            game(-1)
    return 0

# guess == 0
game(-1)
#game(secret_init)
# else:
# return 0

'''
import random
print('---------猜数字游戏！---------')
secret = random.randint(1,100)
guess = 0
while guess !=secret:
    tem = input("I'm thinking of a number! Try to guess the number I'm thinking of:")
    guess = int(tem)
    if guess > secret:
        print('Too hign! Guess again:')
    else:
        print('Too low! Guess again:')
if guess == secret:
    print("That's it! Would you like to play again?(yes/no)")
'''
    
