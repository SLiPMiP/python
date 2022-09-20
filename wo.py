while True:
    print()
    print('Programs:')
    programs = ['Conv', 'Porto', 'Las']
    print(str(programs), ', exit')
    print()
    print('input the title of the program youd like to use or type exit.')

    keyword = input()

    if keyword == 'exit':
        break

    elif keyword in ['Conv', 'conv']:
        euro = 7.43
        minFee = 0.02
        print()
        print('Conversion program started.')
        print('this is a program that converts DKK to EURO.')
        print('there is a 2% fee for converting, at a minimum of 0.5 euro.')
        print('if the fee is less than 0.5 eur, we will not convert your currency.')
        print()
        print('input DKK:')
        while True:
            dkk = input()
            if dkk == 'back':
                print()
                print('Programs:')
                print(programs, ' exit')
                break
            else:
                print()
                print('That is:')
                dkk = float(dkk)
                print(dkk/euro, 'euro')
                print('Conversion fee:')
                if dkk/euro*minFee > 0.5:
                    print(dkk/euro*minFee)
                else:
                    print('0.5')
            print('input another amount to convert, or type back.')

    elif keyword in ['Porto', 'porto']:
        print()
        print('Porto program started')
        print('this program will calculate the price it will cost you to send a letter from denmark to another country, also know as "A Prioritare"')
        print()
        print('input weight in grams')
        while True:
            grams = input()
            print()
            if grams == 'back':
                print()
                print('Programs:')
                print(programs, ' exit')
                break
            else:
                grams = float(grams)
                if grams <= 100:
                    print('you will pay:')
                    print('29.00')
                elif grams <= 250:
                    print('you will pay:')
                    print('58.00')
                elif grams <= 2000:
                    print('you will pay:')
                    print('87.00')
                elif grams > 2000:
                    print('your package it too large for us to handle')
            print()
            print('input another amount, or type back.')

    elif keyword in ['Las', 'las']:
        print()
        print('L.A.S.   I N I T I A T E D')
        print('feed this program any set of numbers and it will tell you which is the biggest and smallest number.')
        print()
        print('Input numbers')
        while True:
            numbers = input()
            if numbers == 'back':
                print()
                print('Programs:')
                print(programs, ' exit')
                break
            print()

            numbers = numbers.split()
            i = 0
            while i < len(numbers):
                numbers[i] = float(numbers[i])
                i = i+1
            small = numbers[0]
            big = numbers[0]
            i = 0
            while i < len(numbers):
                if numbers[i] < small:
                    small = numbers[i]
                if numbers[i] > big:
                    big = numbers[i]
                i = i+1
            print('smallest', small)
            print('biggest number', big)
            print()
            print('input another set of numbers, or type back')
