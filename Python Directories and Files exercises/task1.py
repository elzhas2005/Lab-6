import os
def listx(x):
    directories = []
    files = []

    for item in os.listdir(x):
        full = os.path.join(x, item)

        if os.path.isdir(full):
            directories.append(item)
        else:
            files.append(item)

    return directories, files
print(listx(y))