row_count = 0

FILE = 'access.log'

with open(FILE) as f:
    lines = f.readlines()
    for row in lines:
        row_count += 1

# print(row_count)
# print(type(lines))
# print(dir(lines))

print(lines.__sizeof__())

def gen():
    for i in range(10000):
        yield i

mygen = gen()
print(mygen)

# for i in mygen:
#     print(i)

def greader(file):
    for row in open(file):
        yield row

row_count = 0

mygen = greader(FILE)

for item in mygen:
    row_count += 1

# print(row_count)
# print(type(mygen))
# print(dir(mygen))

print(mygen.__sizeof__())

def infinity_seq():
    n = 0
    while True:
        yield n
        n += 1
# for i in infinity_seq():
#     print(i, end='')


seq_list = [n**2 for n in range(10000)]
seq_gen = (n**2 for n in range(10000))

# print(seq_list.__sizeof__())
# print(seq_gen.__sizeof__())

row_count = 0

mygen = (row for row in open(FILE))

for item in mygen:
    row_count += 1

print(row_count)
print(type(mygen))
# print(dir(mygen))




wwwlog = open("my.log")
bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')
print("Total", sum(bytes))
