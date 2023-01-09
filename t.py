import random

guess = 0
hint = ''
text = 'You guessed: {guess}, '

print('Would you like to guess a number?\n')

while True:

    keyWord = input()

    if 'n' in keyWord.lower():
        if 'y' in keyWord.lower():
            print('what?\n would you or would you not like to guess a number?')
        else:
            print()
            print('Goodbye\n')
            break

    elif 'y' in keyWord.lower():
        if 'n' in keyWord.lower():
            print('what?\n would you or would you not like to guess a number?')
        else:
            print()
            number = random.randint(1, 100)
            print('im thinking of a whole number below 100, guess away!\n')
            print(f'cheatman{number}')

            while True:
                guess = input()
                if int(guess) == number:
                    hint = 'this'
                elif int(guess) < number:
                    hint = 'a bigger'
                elif int(guess) > number:
                    hint = 'a smaller'
                text2 = f'Im thinking of {hint} number. '
                print(text.format(guess=guess), text2, '\n')
