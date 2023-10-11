from Model_Elements.Poligonal_Model import Poligonal_Model
from Model_Elements.Scene import Scene
from Model_Elements.Flash import Flash
from Model_Elements.Camera import Camera

class Model_Store:
    def __init__(self):
        self.models = Poligonal_Model()
        self.scenes = Scene()
        self.flashes = Flash()
        self.cameras = Camera()
        self._change_observers = []
        
    def get_scene(id_: int):
        pass