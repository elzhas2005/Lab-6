import os
def fun(x):
    if not os.path.exists(x):
        print("File not found.")
        return false

    with open(x, 'r') as file:
        z = len(file.readlines())
    
    return z