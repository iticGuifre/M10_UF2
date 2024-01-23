
import json
class User:
    def __init__(self, nom, pes, altura, amplada, fuma, beu):
        self.nom = nom
        self.pes = pes
        self.altura = altura
        self.amplada = amplada
        self.fuma = fuma
        self.beu = beu

    def get_nom(self):
        return self.nom
    def set_nom(self, nom):
        self.nom = nom

    def get_altura(self):
        return self.altura
    def set_altura(self, altura):
        self.altura = altura

    def get_amplada(self):
        return self.amplada
    def set_amplada(self, amplada):
        self.amplada = amplada

    def get_pes(self):
        return self.pes
    def set_pes(self, pes):
        self.pes = pes

    def get_color(self):
        return self.fuma
    def set_fuma(self, fuma):
        self.fuma = fuma

    def get_beu(self):
        return self.beu
    def set_beu(self, beu):
        self.beu = beu

    def salutacio(self):
        print(f"{self.nom}, {self.pes}, {self.altura}, {self.amplada}, {self.fuma}, {self.beu}")

    def to_dict(self):
        dict = {"nom": self.nom, "pes": self.pes, "altura": self.altura, "amplada": self.amplada, "fuma": self.fuma, "beu": self.beu}
        json_text = json.dumps(dict)
        print(json_text)


user = User("Guifré", 75, 175, 1.2, False, True)
user.salutacio()
user.set_pes(80)
user.salutacio()
user.to_dict()
