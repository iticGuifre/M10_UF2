input_num = int(input("Introdueix un numero del 1 al 12, amb el 0 surts del bucle: "))
mesos = ("gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre")
while input_num != 0:
    print(mesos[input_num - 1])
    input_num = int(input("Introdueix un numero del 1 al 12, amb el 0 surts del bucle: "))
