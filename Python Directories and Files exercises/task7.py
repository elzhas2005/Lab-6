import os
def fun(x, y):
    if not os.path.exists(x):
        print(f"Файл '{x}' не существует.")
    with open(x, 'r') as s:
        file = s.read()
    with open(y, 'w') as z:
        z.write(file)