print('Programs:')
progs=['Conv','Porto','Lam']
print(progs)


while True:


    if input()=='Conv':
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
            if dkk=='back':
                break
            else:
                print()
                print('That is:')
                dkk=float(dkk)
                print(str(dkk/euro),'euro')
                print('Conversion fee:')
                if dkk/euro*minFee>0.5:
                    print(dkk/euro*minFee)
                    print()
                else:
                    print('0.5')
                    print()                
    elif input()=='Porto':
        print('Porto program started')
        while True:
            print()
            print('this program will calculate the price it will cost you to send a letter from denmark to another country, also know as "A Prioritare"')
            print()
            print('input weight in grams')
            grams=input()
            print()
            if grams >=100:
                print('you will pay:')
                print('29.00')
            if grams >=250:
                print('you will pay:')
                print('58.00')
            if grams >=2000:
                print('you will pay:')
                print('87.00')


    elif input()=='LAM':
        print('"Largest And Smallest" number detector started')
        while True:
            print('poop')


