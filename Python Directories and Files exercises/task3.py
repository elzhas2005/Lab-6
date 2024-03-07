import os

def fun(x):
    if os.path.exists(x):
        print("The path exists")
        directory, namef = os.path.split(x)
        print(directory)
        print(namef)
    else:
        print("false")
path_to_check = "/path/to/your/file.txt"
fun(y)