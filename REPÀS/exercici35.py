def frase(frase):
    splitted = frase.split()
    dict = {}
    for word in splitted:
        caracters = 0
        for letter in word:
            caracters += 1
        dict[word] = caracters
    print(dict)