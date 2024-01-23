def iva(amount, iva):
    if iva != 4 and iva != 10 and iva != 21:
        iva = 21
    print(amount)
    print(amount * iva / 100)
    print(amount + amount * iva / 100)