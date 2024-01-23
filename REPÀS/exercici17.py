frase = input("Introdueix una frase: ")
llista = []
for caracter in frase:
    if caracter not in llista:
        llista.append(caracter)
print(tuple(llista))