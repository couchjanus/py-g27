# def fibo(n):
#     a = b = 1
#     res = [] 
#     for i in range(n):
#         res.append(a)
#         a, b = b, a + b 
#     return res

def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# for i in fibo(1000000):
#     print(i, end='')

def myrange(start, stop, step=1):
    x = start
    while x < stop:
        yield x
        x += step

# for n in myrange(1, 444, 2):
#     print(n, end='')

print(list(myrange(1, 444, 2)))