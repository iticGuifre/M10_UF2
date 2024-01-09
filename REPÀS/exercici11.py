numero = int(input("Introdueix un nombre entre 10 i 100"))
llista = []
for x in range(numero):
    llista.append(x + 1)

print(tuple(llista))