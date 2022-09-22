while True:
    programs = ['Countdown', 'Additive', 'Multiplication', 'Function']
    print()
    print('Programs')
    print(programs, ' Exit')

    keyword = input()

    if keyword.lower() in ['countdown', 'count', '1']:
        print()
        print('Self destruct initiated.')
        print('M E L T D O W N     E M I N E N T')
        print()
        print('How long time would you like to have to escape?')
        maxTime = float(input())
        countDown = maxTime

        for i in range(maxTime):
            print(countDown)
            countDown = countDown-1
        print('KABOOM')

    elif keyword.lower() in ['additive', 'add', '2']:
        print()
        print('Addition program intiated')
        print('this program adds 0+1+2+3+4.... and you define how many times it does so.')
        print()
        print('input the amount of times youd like the program to run')
        times = int(input())
        print()
        j = 1
        # i=1
        # while i<=n:
        #     j=j+i
        #     print(j)
        #     i=i+1

        for i in range(times):
            j = j+i
            print(j)

    elif keyword.lower() in ['multiplication', 'mult', '3']:
        print()
        print('Multiplication table program started.')
        print('this program generates a multiplication table with a given value as the smallest value.')
        print()
        print('input multiplication root and the size of the multiplication table')
        n = input()
        n = n.split()
        i = 1
