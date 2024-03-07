import os

def fun(x):
    if os.path.exists(x) and os.access(x, os.W_OK):
        os.remove(x)
    else:
        print("false")
fun(y)
