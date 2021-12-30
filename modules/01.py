import os
import io, contextlib

# item = 'repo'
# if os.path.exists(item):
#     os.chdir(item)
# else:
#     os.mkdir(item)
#     os.chdir(item)
#     print(os.getcwd())

# print(os.getcwd())

# if not os.path.exists('first'):
#     os.makedirs('first/second/third')
# else:
#     os.removedirs('first/second/third')

zen = io.StringIO()

with contextlib.redirect_stdout(zen):
    import this

with open('zen.txt', 'w') as f:
    print(zen.getvalue(), file=f)


ZEN = 'python_zen'

if not os.path.exists(ZEN):
    os.mkdir(ZEN)

n = 1
with open('zen.txt') as f:
    for line in f:
        os.mkdir(ZEN+'/zen'+str(n))
        with open(ZEN+'/zen'+str(n)+'/zen'+str(n)+'.txt', 'a') as fz:
            print(line, file=fz)
        n += 1 
