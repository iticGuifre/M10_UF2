def compra(dict, iva):
    keys = dict.keys()
    amount = 0
    for key in keys:
        amount += key + key * dict[key] / 100
    print(amount + amount * iva / 100)

