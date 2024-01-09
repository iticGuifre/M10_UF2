numero = int(input("Introdueix un nombre: "))
taula = ""
for x in range(10):
    taula += str(x * 3) + ", "
print(taula[:-2])