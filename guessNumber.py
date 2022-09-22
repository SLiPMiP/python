import random
print('Would you like to guess a number?\n')
while True:
    keyWord = input()
    if 'n' in keyWord.lower():
        print()
        print('Goodbye\n')
        break
    elif 'y' in keyWord.lower():
        print()
        number = random.randint(1, 100)
        print('im thinking of a whole number below 100, guess away!\n')
        print(number)
        while True:
            guess = int(input(f'your guess: '))
            if guess == number:
                print(f'nice! you guessed the number! {number}\n')
                break
            elif guess < number:
                print('bigger, my number is.\n')
            elif guess > number:
                print('smaller, my number is\n')
    print('Would you like to guess another number?')
