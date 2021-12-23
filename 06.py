squares = []

# for x in (1,2,3,4,5,6,7,8,9,10):
#     squares.append(x*x)

squares = [i*i for i in range(1, 11)]

# print(squares)

word = 'comprehention'
s = []
for i in word.upper():
    s.append(i)
    
# print([st.upper() for st in word])

# print([w.strip(',') for w in ['the,','word,,','mostly','have, commas,' ]])


# sentence = "Although. that way may not be obvious. at first unless. you're Dutch. Now is better than never."
# tmp = ";".join([word.strip('.') for word in sentence.split('.')])
# print(tmp)
# print(["".join(sorted(word, key=lambda x: x.lower())) for word in sentence.split()])


# print([x  for x in range(100) if x % 2 == 0])

# print([x  if x % 2 == 0 else None for x in range(100)])

# print([2*(x if x % 2 == 0 else -1) + 1 for x in range(100)])

n = []
for x in range(100):
    if x%2 == 0:
        t = x
    else:
        t = -1
    n.append(2*t+1)
# print(n)

# print([x + y for x in range(10) if x > 5 for y in range(5,10)])

# print([x + y for x in range(10) for y in range(5,10) if x > 5])

from string import ascii_letters

letters = 'aаtйqєwжeїrіtиy'

res = [letter if letter in ascii_letters else '_' for letter in letters]

# print(res)

# print([i if i > 0 else 0 for i in [1.33, -3.2, 44.6, 7.88, -1.2, -3.22, 5]])

# print([x + y for x, y in [(1,2), (3,4), (5,7)]])

# print([x + y + z for x, y, z in zip([1,2,3,5], [3,4,8,7], [7,5,7,6])])

# print(sum(
#     1 for x in range(10000)
#     if x%2 == 0 and '9' in str(x)
# ))

# print(list(map(float, ['1', '4', '6', '77', '33'])))

d1 = {1: 'a', 2: 'b', 3: 'c'}

# print({ v: k for k,v in d1.items() })
# print(dict((v,k) for k,v in d1.items()))
# print(dict(zip(d1.values(), d1)))
# print(dict(zip(d1.values(), d1.keys())))
# print(dict(map(reversed, d1.items())))
map(reversed, d1.items())
d1 = dict(map(reversed, d1.items()))
d2 = {9: 'a', 6: 'b', 5: 'd'}
d2 = dict(map(reversed, d2.items()))

# print({k:v for d in [d1, d2] for k,v in d.items()})

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(m)
# print([[r[i] for r in m] for i in range(len(m))])

l1 = [1,2,3,4]
l2 = ['a','b','c','d']

print([(i,j) for i,j in zip(l2,l1)])
from functools import reduce

print(reduce(lambda x,y: x+y, l1))