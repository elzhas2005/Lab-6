import os
def fun(x,y):
    with open(x, 'w') as file:
        file.writelines(f"{i}\n" for i in y)
fun(x,y)