from time import sleep
import os

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        sleep(0.05)
    print()

def main():
    sys = 'System \t: '
    sysg = 'Hello, how are you? I hope you are always happy and healthy.'
    sysa1 = 'Before we start, please let me know your name.'
    ask = 'Do you want to start this conversation? (y/n) '
    frwl = 'Okay, see you next time.'
    frwl1 = 'Okay, my time is up. See you next time.'
    grt = 'So, your name is '
    ask1 = 'Please give me a nickname:'
    Y = 'Why do you look so sad today?'
    A = 'I think you need to talk to someone, like your family, friend, or best friend.'
    i = 'You need to find a way to resolve your problem, buddy.'
    i1 = 'I hope you can resolve your problem with someone.'
    so = 'So, my name is '
    so2 = 'It is a beautiful name.'
    thnks = 'Thank you '
    so1 = ', I like it.'
    use = 'Username \t: '
    us0 = 'User \t: '
    titik2 = "\t: "
    cm = ','
    gtw = 'Don\'t worry, you have good friends around you.'
    lg = 'Input your account \t: '
    sg = 'Input something to create your account \t: '
    pw = 'Input your password \t: '
    mpw = 'Input something to create your password \t: '
    strt = 'Starting system....'
    make = 'Creating your account......'
    dn = 'Done.....!'
    err = '404 not found'
    srp = 'What do you like to talk about today? (e.g., hobbies, movies, dreams)'

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
        print_slow('')
        print_slow(name_sys)
        print_slow(titik2)
        print_slow(srp)
        print_slow('')

        print_slow(name_sys)
        print_slow(titik2)
        print_slow(frwl1)
        print('')

if __name__ == "__main__":
    main()
