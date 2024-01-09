import random

aleatori = random.randint(1, 100)
print(aleatori)

numInput = int(input("Introdueix un numero: "))

while numInput != aleatori:
    if numInput < aleatori:
        print("El nombre que busques és més gran")
    if numInput > aleatori:
        print("El nombre que busques és més petit")
    numInput = int(input("Introdueix un numero"))

print("Has trobat el numero, és el " + str(aleatori))