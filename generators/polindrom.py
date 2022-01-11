def is_polindrome(n):
    if n // 10 == 0:
        return False
    tmp = n
    rev_n = 0
    while tmp != 0:
        rev_n = (rev_n * 10) + (tmp % 10)
        tmp = tmp // 10

    if n == rev_n:
        return n 
    else: return False


def inf_s():
    n = 0
    while True:
        yield n 
        n += 1

# for i in inf_s():
#     p = is_polindrome(i)
#     if p:
#         print(p, end=' ')


import cProfile

cProfile.run('sum([i*i for i in range(10000)])')

cProfile.run('sum((i*i for i in range(10000)))')