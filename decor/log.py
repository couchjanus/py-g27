from json import load


def logger(f):
    def wrapper():
        print('Start here')
        f()
        print('End here')
    return wrapper


@logger
def foo():
    print("... I'm foo function and I'v run...")
    
foo()