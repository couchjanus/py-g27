import os

print(os.getcwd())

fn = input('Enter file name: ')

if os.path.exists(fn):
    print(os.getcwd())
    print(__file__)

    print(os.path.basename(__file__))
    print(os.path.dirname(__file__))
    print(os.path.abspath(__file__))

    print(os.path.getatime(__file__))

    print(os.path.getmtime(__file__))
    print(os.path.getctime(__file__))

    print(os.path.getsize(__file__))
    print(os.path.realpath(__file__))
    print(os.path.isdir(__file__))
    print(os.path.isabs(__file__))



    

else:
    print(os.getcwd())