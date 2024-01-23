ftotal = input('Introdueix el preu de tot el carrito: ')
iva = input("Introdueix l'iva")
def amb_iva(ftotal, iva = 21):
    ftotal = ftotal * iva
    return ftotal
print(amb_iva(ftotal, iva))


