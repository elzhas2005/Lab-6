import string

def fun():
    alphabet = string.ascii_uppercase
    for l in alphabet:
        name = f"{l}.txt"
        with open(name, 'w') as file:
            file.write(f"Это файл {l}.txt")
fun(y)