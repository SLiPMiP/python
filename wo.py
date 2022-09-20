print('Programs:')
programs = ['Conv', 'Porto', 'Lam']
print(programs, ' exit')


while True:

    keyword = input()

    if keyword == 'exit':
        break

    elif keyword == 'Conv':
        euro = 7.43
        minFee = 0.02
        print()
        print('Conversion program started.')
        print('this is a program that converts DKK to EURO.')
        print('there is a 2% fee for converting, at a minimum of 0.5 euro.')
        print('if the fee is less than 0.5 eur, we will not convert your currency.')
        print()
        while True:
            print('input DKK')
            dkk = input()
            if dkk == 'back':
                break
                print('Programs:')
                print(programs, ' exit')
            else:
                print()
                print('That is:')
                dkk = float(dkk)
                print(str(dkk/euro), 'euro')
                print('Conversion fee:')
                if dkk/euro*minFee > 0.5:
                    print(dkk/euro*minFee)
                    print()
                else:
                    print('0.5')
                    print()

    elif keyword == 'Porto':
        print()
        print('Porto program started')
        print('this program will calculate the price it will cost you to send a letter from denmark to another country, also know as "A Prioritare"')
        print()
        while True:
            print('input weight in grams')
            grams = input()
            print()
            if grams == 'exit':
                break
                print('Programs:')
                print(programs, ' exit')
            else:
                if grams >= '100':
                    print('you will pay:')
                    print('29.00')
                elif grams >= '250':
                    print('you will pay:')
                    print('58.00')
                elif grams >= '2000':
                    print('you will pay:')
                    print('87.00')

    elif keyword == 'LAM':
        print('"Largest And Smallest" number detector started')
        while True:
            print('Input numbers')
