import json

dict = {}
llista = []
for x in range(4):
    title = input("Afegeix titol: ")
    cover = input("Afegeix portada: ")
    year = input("Afegeix any: ")
    pages = input("Afegeix pagines: ")
    dict["book"] = {"title": title, "cover": cover, "year": year, "pages": pages}
    llista.append(dict)

dict_final = {"books": [llista[0], llista[1], llista[2], llista[3]]}
print(dict_final)
with open("exercici23.json", "w") as file:
    json.dump(dict_final, file)
