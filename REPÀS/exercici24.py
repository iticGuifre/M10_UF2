import json
with open("exercici23.json", "r") as file:
    readed = file.read()
    file.close()

jsonLoaded = json.loads(readed)
print(jsonLoaded)
