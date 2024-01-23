
import json
class Vehicle:
    def __init__(self, pes, altura, amplada, num_rodes, color, places):
        self.pes = pes
        self.altura = altura
        self.amplada = amplada
        self.num_rodes = num_rodes
        self.color = color
        self.places = places

    def get_pes(self):
        return self.pes
    def set_pes(self, pes):
        self.pes = pes

    def get_altura(self):
        return self.altura
    def set_altura(self, altura):
        self.altura = altura

    def get_amplada(self):
        return self.amplada
    def set_amplada(self, amplada):
        self.amplada = amplada

    def get_num_rodes(self):
        return self.num_rodes
    def set_num_rodes(self, num_rodes):
        self.num_rodes = num_rodes

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

    def get_places(self):
        return self.places
    def set_places(self, places):
        self.places = places

    def parts(self):
        print(f"{self.pes}, {self.altura}, {self.amplada}, {self.num_rodes}, {self.color}, {self.places}, ")

    def to_dict(self):
        dict = {"pes": self.pes, "altura": self.altura, "amplada": self.amplada, "num_rodes": self.num_rodes, "color": self.color, "places": self.places}
        json_text = json.dumps(dict)
        print(json_text)


vehicle = Vehicle(15, 10, 5, 4, "blanc", 5)
vehicle.parts()
vehicle.set_places(4)
vehicle.parts()
vehicle.to_dict()
