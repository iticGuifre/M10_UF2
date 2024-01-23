contactes = {'Roger': 678232311, 'Oriol': 566879326}
def elimina(contactes_atr, user):
    contactes_atr.pop(user)
    return contactes

print(elimina(contactes, 'Roger'))
