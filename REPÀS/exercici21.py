numeros = input("Insereix 10 numeros separats per espais: ")
splitted = numeros.split()
suma = 0
for x in range(len(splitted)):
    splitted[x] = int(splitted[x])
    suma += splitted[x]
print(splitted)
print(suma)
