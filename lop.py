while True:
    programs = ['Countdown', 'Additive', 'Multiplication', 'Function']
    print()
    print('Programs')
    print(programs, ' Exit')
    print('type the title of the program youd like to start')
    keyword = input()

    if keyword.lower() in ['countdown', 'count', '1']:
        print()
        print('Self destruct initiated.')
        print('M E L T D O W N     E M I N E N T')
        print()
        print('How long time would you like to have to escape?')
        while True:
            maxTime = input()
            if maxTime == 'back':
                break
            else:
                maxTime = int(maxTime)
                countDown = maxTime
                for i in range(maxTime):
                    countDown = countDown-1
                    print(countDown)
                print('KABOOM')
                print('lmao gotcha')
            print()
            print('input another amount to run the program again or type back')

    elif keyword.lower() in ['additive', 'add', '2']:
        print()
        print('Addition program intiated')
        print('this program adds 0+1+2+3+4.... and you define how many times it does so.')
        print()
        print('input the amount of times youd like the program to run')
        while True:
            times = int(input())
            if input == 'back':
                break
            else:
                print()
                j = 1
                for i in range(times):
                    j = j+i
                    print(j)
            print()
            print('input another amount to run the program again or type back.')

    elif keyword.lower() in ['multiplication', 'mult', '3']:
        print()
        print('Multiplication table program started.')
        print('this program generates a multiplication table with a given value as the smallest value.')
        print()
        print('input multiplication root and the size of the multiplication table')
        while True:
            n = input()
            print()
            if input == 'back':
                break
            else:
                n = n.split()
                number = float(n[0])
                tableLength = int(n[1])
                for i in range(tableLength+1):
                    if i >= 1:
                        print(number*i)
            print()
            print('input another set of numbers to run the program again og type back')

    elif keyword.lower() in ['function', 'funct', '4']:
        print()
        print('function program started')
        print('this program calculates the f value of the function "f(x) = x3^2 + 6x + 9, starting at "x=1"')
        print()
        print('input the amount of times the program should run')
        while True:
            x = input()
            if x == 'back':
                break
            else:
                x = int(x)
                oneLiner = []
                secondLiner = ''
                for i in range(x+1):
                    if i > 0:
                        print(f'f({i}) = {i*3**2+6*i+9}')
                        oneLiner.append(f'f({i}) ={i*3**2+6*i+9}')
                        secondLiner = secondLiner+f'f({i}) = {i*3**2+6*i+9}, '
                # print(oneLiner)
                print(secondLiner)
