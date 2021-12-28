# fh = open('test.txt', 'ab')

# print(type(fh))

# print(dir(fh))

# print(fh.name)
# print(fh.closed)
# print(fh.mode)
# print(fh.fileno())
# fh.close()
# print(fh.closed)

try:
    fh = open('test2.txt', 'a')
    try:
        fh.write("Hello world")
    except Exception as e:
        print(e)
    finally:
        fh.close()
except Exception as e:
    print(e)