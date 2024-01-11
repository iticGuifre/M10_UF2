numero = int(input("Introdueix nombre: "))
llista = []
while numero != 0:
    llista.append(numero)
    numero = int(input("Introdueix nombre: "))

llistaOrdenada = sorted(llista)
print(llistaOrdenada)
