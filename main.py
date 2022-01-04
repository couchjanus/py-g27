import sys

from crlf import to_lin, to_win

def main():

    help = '''
        Use: {}  <file name> lw
        Use: {}  <file name> wl
    '''

    if len(sys.argv) < 3:
        print('Too few params')
        print(help.format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

    if sys.argv[2] == 'lw':
        to_win(sys.argv[1])
    elif sys.argv[2] == 'wl':
        to_lin(sys.argv[1])
    else:
        print('Error: Unknown paraneter {}'.format(sys.argv[2]))

if __name__ == '__main__':
    main()