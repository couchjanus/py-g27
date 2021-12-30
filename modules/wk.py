import os

def walk(param):

    files = []
    dirs = []
    d = {}

    for root, dirnames, filenames in os.walk(os.getcwd() + '/' + param):
        for subdir in dirnames:
            d = {
                'path': os.path.join(root, subdir)
            }
            dirs.append(d)

        for file in filenames:
            d = {'path': os.path.join(root, file)}
            files.append(d)

    return dirs, files
