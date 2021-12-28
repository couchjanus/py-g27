
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

with open('test2.txt', 'w') as fh:
    fh.write("Hello world with context manager")
