import math

# def foo():
#     # pass
#     print("Hello function")
#     # return True
#     return 123

# foo()
# print(foo())

# def bar(a = 100, b = 100):
#     return a + b

# print(bar(55, 88))
# print(bar(55))
# print(bar())

# False
# print('''Hello''' == """Hello""")

# print(2**1000000000)

x = 0
y = 0
o = '+'

TITLE = 'Calculator'

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def div(x, y):
    return x / y

def sin(x):
    return math.sin(x)


# o = input('Enter operation = ')

# if o == '+':
#     print(plus(x, y))
# elif o == '-':
#     print(minus(x, y))
# elif o == '/':
#     print(div(x, y))
# else:
#     print('Bed operation')

def menu():
    print("Operations:")
    print("Add: +")
    print("Subtr: -")
    print("Div: /")
    print("Sin: s")
    print("Exit: q")
    return input('Your choice (+|-|/|q):')

while True:
    if o == 'q':
        print('Thank You for using ' + TITLE + '!')
        break
    x = int(input('Enter x = '))
    if o != 's':
        y = int(input('Enter y = '))

    match o:
        case '+':
            print(plus(x, y))
        case '-':
            print(minus(x, y))
        case '/':
            print(div(x, y))
        case 's':
            print(sin(x))
        case _:
            print('Bed operation')