import random
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
            print('ok, im thinking of a whole number below 100, guess away!\n')
            print(number)
            while True:
                guess = int(input(f'your guess: '))
                if guess == number:
                    print(f'nice! you guessed the number! {number}!\n')
                    break
                elif guess < number:
                    print('bigger, my number is.\n')
                elif guess > number:
                    print('smaller, my number is\n')
        print('Would you like to guess another number?')
