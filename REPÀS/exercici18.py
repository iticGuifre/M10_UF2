frase = input("Introdueix 2 paraules: ")
splitted = frase.split()
tupla = tuple(splitted)
dict = {}

for paraula in tupla:
    for caracter in paraula:
        if caracter in dict.keys():
            dict[caracter] += 1
        else:
            dict[caracter] = 1
print(dict)