from Poligon import Poligon
from Texture import Texture

class Poligonal_Model:
    def __init__(self, textures: Texture): # композиция - poligons, агрегация textures
        self.poligons = Poligon()
        if not self.poligons:
            raise f'Должен быть хотя бы 1 объект {Poligon} в {self.poligons}'
        self.textures = textures