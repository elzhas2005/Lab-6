import time
import math
x = float(input())
y = float(input())
def fun(a,b):
    time.sleep(b/1000)
    return math.sqrt(a)
print(fun(x,y))