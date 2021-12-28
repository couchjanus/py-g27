
with open('test2.txt', 'r', encoding='utf8') as fh:
    # text = fh.read()
    print(fh.readline())
    print(fh.readline())

# print(text)


with open('test2.txt', 'r', encoding='utf8') as fh:
    for line in fh:
        print(line)

with open('test2.txt', 'r', encoding='utf8') as fh:
    line = fh.readline()
    while line:
        print(line, end='')
        line = fh.readline()

with open('test2.txt', 'r', encoding='utf8') as fh:
    lines = fh.readlines()

print(lines[3])