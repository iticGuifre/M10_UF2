areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
print(areas_pis[2:4])
print(areas_pis[-2:])
print(areas_pis[6:8])
print(areas_pis[:3])
print(areas_pis[2:])
print(areas_pis[5] + areas_pis[-1])
areas_pis[9] = 10
print(areas_pis)
areas_pis.append("pati interior")
areas_pis.append(2.78)
print(areas_pis)
metres = 0
for x in range(len(areas_pis)):
    if x % 2 == 1:
        metres += areas_pis[x]
print(metres)