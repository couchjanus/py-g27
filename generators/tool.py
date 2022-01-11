import itertools

def gen1():
    counter = itertools.count()
    while True:
        yield next(counter)

# for item in gen1():
#     print(item, end=" ")
#     if (item == 3):
#         gen1().close()


# профилировщик памяти от PyPi: pip install memory-profiler
# Функция perf_counter() возвращает значение времени счетчика производительности. Включает время, прошедшее с времени sleep, и является общесистемным. 
from time import perf_counter

n, m = map(int, input('input 2 integer in single line: ').split())

start = perf_counter()

for i in range(n):
    t = int(input('input n times: ')) # user gave input n times
    if t % m == 0:
        print(t)

stop = perf_counter()

print("Elapsed time:", stop, start)

print("Elapsed time during the whole program in seconds:", stop - start)








