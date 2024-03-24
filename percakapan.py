from time import sleep
import os

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        sleep(0.05)
    print()

def main():
    sys = 'system \t: '
    sysg = 'hello, how are you? I hope u always happy and healthy'
    sysa1 = 'before we start the talks, let me know ur name'
    ask = 'do you want to start this depression talks? (y/n) '
    frwl = 'okay see you next time'
    frwl1 = 'okay my time was done, see you next time'
    grt = 'so ur name is '
    ask1 = 'make some nickname for me, please'
    Y = 'why you look so sad today?'
    A = 'i think u need to talk with somebody, like ur family or ur friend, maybe ur best friend?'
    i = 'u need to find ur way to resolve ur problem buddy'
    i1 = 'i hope u can resolve ur problem with somebody'
    so = 'so, my name is '
    so2 = 'is a beautifull name'
    thnks = 'thankyou '
    so1 = ' i like it'
    use = 'username \t: '
    us0 = 'user \t:'
    titik2 = "\t: "
    cm = ','
    gtw = 'dont worry u have a good friend around u'
    lg = 'input your account\t: '
    sg = 'input something to make your account \t:'
    pw = 'input your password\t:'
    mpw = 'input something to make your password \t:'
    strt = 'starting system....'
    make = 'making your account......'
    dn = 'done.....!'
    err = '404 not found'

    print_slow(sg)
    lgn = input(" ")
    data_acc = lgn
    print_slow(mpw)
    make_pw = input(' ')
    data_pw = make_pw

    os.system('cls' if os.name == 'nt' else 'clear')

    print_slow(make)
    print('')
    print_slow(dn)

    os.system('cls' if os.name == 'nt' else 'clear')
    print_slow(strt)
    print('')
    print_slow(dn)

    os.system('cls' if os.name == 'nt' else 'clear')

    print_slow(ask)
    yon = input('')

    if yon == 'n':
        print_slow(frwl)

    if yon == 'y':
        print_slow(sys)
        print_slow(sysg)
        print_slow(sys)
        print_slow(sysa1)

        us1 = input(us0)
        name_data = us1

        print_slow(sys)
        print_slow(grt)
        print_slow(name_data)

        print_slow(sys)
        print_slow(ask1)

        sus = input('\t: ')
        name_sys = sus

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(so)
        print_slow(name_sys)
        print_slow('')
        print_slow(name_sys)
        print_slow(titik2)
        print_slow(so2)
        print_slow(cm)
        print_slow(so1)
        print_slow('')
        print_slow(name_data)
        input('\t: ')

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(Y)
        print_slow('')
        input('')

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(A)
        print_slow('')
        input('')

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(i)
        print_slow('')
        print_slow(name_sys)
        print_slow(titik2)
        print_slow(i1)
        print_slow('')
        print_slow(name_data)
        input('\t: ')

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(gtw)
        print('')
        print_slow(name_sys)
        print_slow(titik2)
        print_slow(frwl1)
        print('')

if __name__ == "__main__":
    main()
