import create, read, update, delete

print("a) crear (diametre, color, pes, forma, esRugosa, material)")
print("b) llegir")
print("c) actualitzar (diametre, color, pes, forma, esRugosa, material)")
print("d) eliminar (diametre)")

entrada = input()
while entrada != "a" and entrada != "b" and entrada != "c" and entrada != "d":
    entrada = input("Incorrecte")

if entrada == "a":
    diametre = int(input("Introdueix diametre: "))
    color = input("Introdueix color: ")
    pes = int(input("Introdueix pes: "))
    forma = input("Introdueix forma: ")
    esRugosa = bool(input("Introdueix si es rugosa:"))
    material = input("Introdueix material: ")
    create.crear(diametre, color, pes, forma, esRugosa, material)

if entrada == "b":
    read.llegir()

if entrada == "c":
    diametre = int(input("Introdueix diametre: "))
    color = input("Introdueix color: ")
    pes = int(input("Introdueix pes: "))
    forma = input("Introdueix forma: ")
    esRugosa = bool(input("Introdueix si es rugosa:"))
    material = input("Introdueix material: ")
    update.actualitza(diametre, color, pes, forma, esRugosa, material)

if entrada == "d":
    diametre = int(input("Introdueix diametre: "))
    delete.elimina(diametre)
