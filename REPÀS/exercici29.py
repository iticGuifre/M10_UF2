def entre():
    num1 = int(input("NUM1: "))
    num2 = int(input("NUM2: "))
    suma = 0
    for x in range(num1, num2 + 1):
        suma += x
        print(x)
    print(suma)

