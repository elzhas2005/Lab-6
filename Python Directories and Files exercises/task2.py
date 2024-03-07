import os

def fun(x):
    if not os.path.exists(x):
        print("Путь не существует.")
    if not os.access(x, os.R_OK):
        print("Нет доступа на чтение.")
    else:
        print("Доступ на чтение.")
    if not os.access(x, os.W_OK):
        print("Нет доступа на запись.")
    else:
        print("Доступ на запись .")
fun(y)