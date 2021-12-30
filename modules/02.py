import os

for root, dirs, files in os.walk('.'):
    print(root)
    for dir in dirs:
        print(dir)

    for file in files:
        print(file)

result = []
for root, dirs, files in os.walk('.'):
    
    for dir in dirs:
        d = {'path': os.path.join(root, dir)}
        result.append(d)
        
print(result)
