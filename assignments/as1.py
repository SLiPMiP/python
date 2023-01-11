print('poop')

def qa(string):
    print(string)
    return ('ja' in input())
    
if qa('er du ved at dø?'):
    if qa('seriøst?'):
        print('ring 1-1-2')
    elif qa('tror du det er alvorligt?'):
        if qa('synes du, forkølelse er alvorligt?'):
            print('ring til din mor')
        elif qa('er din læge åben nu?'):
            print('ring til din egen læge')
        else:
            print('ring til lægevagten')
    print('ring til din mor')
elif qa('tror du det er alvorligt?'):
    if qa('synes du, forkølelse er alvorligt?'):
        print('ring til din mor')
    elif qa('er din læge åben nu?'):
        print('ring til din egen læge')
    else:
        print('ring til lægevagten')
else:
    print('ring til din mor')