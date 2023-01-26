CDEBUG = '\033[32m'
CINFO = '\033[34m'
CWARN = '\033[33m'
CERROR = '\033[31m'
CFATAL = '\033[41m'
CENDC = '\033[0m'



def cprint(text, color):
    print(f'{color}{text}{CENDC}')



if __name__ == '__main__':
    cprint('Hello', CDEBUG)
    cprint('Hello', CINFO)
    cprint('Hello', CWARN)
    cprint('Hello', CERROR)
    cprint('Hello', CFATAL)

    print()
    colors = [4, 7, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105, 106]
    for i in colors:
        print(f'\033[{i}m' + f"[{i}] Hello, This is a colorful text" + CENDC),
