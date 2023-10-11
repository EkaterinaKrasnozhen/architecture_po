from Model_Elements.Poligonal_Model import Poligonal_Model
from Model_Elements.Scene import Scene
from Model_Elements.Flash import Flash
from Model_Elements.Camera import Camera


class Model_Store:
    def __init__(self):
        self.models: list[Poligonal_Model] = []
        self.scenes: list[Scene] = []
        self.flashes: list[Flash] = []
        self.cameras: list[Camera] = []
        if not len(self.models) or not len(self.scenes) or not len(self.flashes) or not len(self.cameras): 
            # можно в одну строку все?
            raise f'Должен быть хотя бы 1 объект  в свойствах'
        self._change_observers = []
        
    def get_scene(id_: int):
        pass