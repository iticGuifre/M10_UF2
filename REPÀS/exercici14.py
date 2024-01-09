numeros = input("Introdueix 10 nombres")
splitted = numeros.split()
llista = []
for number in splitted:
    print(number)
    llista.append(int(number))
llista = sorted(llista)
print(llista)
