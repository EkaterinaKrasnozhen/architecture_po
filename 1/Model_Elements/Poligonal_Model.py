from Poligon import Poligon
from Texture import Texture
from Stuff import Point3D

class Poligonal_Model:
    def __init__(self, textures: Texture): # композиция - poligons, агрегация textures
        self.poligons = list[Poligon]
        self.poligons.append(Poligon(list[Point3D()]))
        self.textures = textures