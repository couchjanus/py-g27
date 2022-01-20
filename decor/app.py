def foo(string, c=123):
    return string.lower()

# print(foo('Hello'))

# foo.hell = 'Hello from hell'
# print(foo.hell)
# foo.c = 5555
# print(foo.c)

# bar = foo
# print(bar('hello var'))


a = [1,2,3,4,5]

sq = lambda x: x*x
print(type(sq))
b = list(map(sq, a))
print(list(map(sq, a)))

print(list(map(lambda x: x*x, [1,2,3,4,5])))

# print(dir(sq))
# __call__ - function

class LowerCall:
    def __call__(self, string):
        return string.lower()
    
# hello = LowerCall()
# print(dir(hello))
# print(type(hello))

# print(hello('HELLO FROM LOWER'))

def foomar(a):
    def helper(b):
        return a * b
    return helper


f1 = foomar(3)
print(type(f1))
print(f1(6))

f2 = foomar(5)
print(type(f2))
print(f2(6))

print(foomar(6)(6))
print(foomar(26)(36))


def call_this(f):
    f()
    print("Called call_this")
    
def call_foo(f):
    f('Hello function')

def call_bar(hello = ''):
    print(hello + " Called call_bar")


call_this(call_bar)
call_foo(call_bar)

def loca(f):
    def wrapper():
        return f().lower()
    return wrapper

def test_loca():
    return 'HELLO DECORATORS WORLD'

print(loca(test_loca)())


def tresp(f):
    def decor(x):
        return f(float(x))
    return decor

def fo(x):
    return x*x

foo_new = tresp(fo)
print(foo_new('7'))

@tresp
def foom(x):
    return x*x

print(foom('7'))

@tresp
def boom(x):
    return x / 77

print(boom('7777'))

