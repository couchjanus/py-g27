import hashlib
import time
import os

files = {}

def walk(path):
    for root, dirnames, filenames in os.walk(path):
        for subdir in dirnames:
            dir = os.path.join(root, subdir)
            for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]:
                hash = hashlib.md5()
                with open(os.path.join(dir, file), encoding='utf-8') as f:
                    for chunk in iter(lambda: f.read(2048), ""):
                        hash.update(chunk.encode('utf-8'))
                md5 = hash.hexdigest()
                if file in files and md5 != files[file]:
                    print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}')
                files[file] = md5

def walking(path):
    for root, dirnames, filenames in os.walk(path):
        for subdir in dirnames:
            dir = os.path.join(root, subdir)
            for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]:
                hash = hashlib.sha256()
                with open(os.path.join(dir, file), encoding='utf-8') as f:
                    for chunk in iter(lambda: f.read(2048), ""):
                        hash.update(chunk.encode('utf-8'))
                sha256 = hash.hexdigest()
                # if file in files and sha256 != files[file]:
                #     print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}')
                files[file] = sha256
    return files

if __name__ == "__main__":
    path = 'python_zen'
    walk(path)
    for k, v in files.items():
        print((k, v))

