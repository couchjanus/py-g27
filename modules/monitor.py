import sys
import os
from hashdir import walk, walking
import time
import shelve

def main():

    help = '''
        Use: {}  <dir name>
    '''

    if len(sys.argv) < 2:
        print('Too few params')
        print(help.format(sys.argv[0]))
        sys.exit(1)

    # while True:
    #     walk(sys.argv[1])
    #     time.sleep(1)

    files = walking(sys.argv[1])

    # for k, v in files.items():
    #     with shelve.open('repo') as r:
    #         r[k] = v

    with shelve.open('repo') as r:
        for k in r.keys():
            print(k)
        for v in r.values():
            print(v)

if __name__ == '__main__':
    main()