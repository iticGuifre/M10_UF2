nom = input("Introdueix nom o 0 per sortir: ")
edat = int(input("Introdueix edat o 0 per sortir: "))
dict = {}
while nom != "0" or edat != 0:
    if nom not in dict.keys():
        dict[nom] = edat
    nom = input("Introdueix nom o 0 per sortir: ")
    edat = int(input("Introdueix edat o 0 per sortir: "))
print(dict)