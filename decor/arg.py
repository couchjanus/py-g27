
def decor(f):
    def wrapper(*args):
        print("{} called with {}".format(f.__name__, [*args]))
        return f(*args)
    
    return wrapper
@decor
def add(a, b):
    return a + b

print(add(77, 99))

from time import sleep

def delay(s):
    def decor(f):
        def wrapper(*args, **kwargs):
            print("{} called with {} and {}".format(f.__name__, [*args], {**kwargs}))
            sleep(s)
            return f(*args, **kwargs)
        return wrapper
    return decor

@delay(5)
def may_be(times, name=''):
    return name + " said: It is nearly Luncheon Time! " * times
            
print(may_be(3, name='Winnie-the-Pooh'))
        
def decor_ret(f):
    def wrapper(*args, **kwargs):
        print("Run method: " + str(f.__name__))
        return f(*args, **kwargs)
    return wrapper

@decor_ret
def calc(v):
    return v**0.5

print(calc(17))