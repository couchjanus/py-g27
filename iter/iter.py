list = [1,2,3,4,5]

# for i in list:
#     print(i)

itr = iter(list)

# print(type(itr)) #<class 'list_iterator'>

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# print(next(itr))

for i in range(5):
    print(next(itr))
print(itr)

for i in range(5):
    print(list[i])
print(list)


for i in range(5):
    print(i)
    i = 7

itr1 = iter(list)
for i in range(15):
    print(i, next(itr1, None))

from random import randint 

def d6():
    return randint(1,6)

for roll in iter(d6, 6):
    print(roll)

def counter():
    x = 0
    def f():
        nonlocal x
        x += 1
        return x
    return f

c = counter()
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())

for i in iter(c, 13):
    print(i)

