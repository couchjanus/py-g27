import sys
# from wk import walk
# from rewolk.wk import walk
from rewalk import wk

def main():
    for i, param in enumerate(sys.argv):
        print('i = {} \tparam = {}'.format(i, param))

    help = '''
        Use: {} name <dir name>
        or:  {} n <dir name> 
    '''

    if len(sys.argv) == 1:
        print('Too few params')
        print(help.format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

    if sys.argv[1] == 'name' or sys.argv[1] == 'n':
        # dirs, files = walk(sys.argv[2])
        dirs, files = wk.walk(sys.argv[2])
        print(dirs)
        print(files)
    else:
        print('Error: Unknown paraneter {}'.format(sys.argv[1]))

if __name__ == '__main__':
    main()