def pop(f):
    def wrapper(*args, **kwargs):
        print('POP iT!')
        return f(*args, **kwargs)
    return wrapper

def lock(f):
    def wrapper(*args, **kwargs):
        print('LOCK iT!')
        return f(*args, **kwargs)
    return wrapper
@pop
@lock
def drop(it):
    print("DROP it")
    return it[:]

print(drop("That's the end of that one, isn't it?"))
