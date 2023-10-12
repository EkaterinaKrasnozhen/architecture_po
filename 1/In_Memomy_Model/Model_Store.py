from zope.interface import implementer
from Model_Elements.Poligonal_Model import Poligonal_Model
from Model_Elements.Scene import Scene
from Model_Elements.Flash import Flash
from Model_Elements.Camera import Camera
from IModel_Changer import IModelChanger
from IModel_Changed_Observer import IModel_Changed_Observer

@implementer(IModelChanger)
class Model_Store(IModel_Changed_Observer):
    def __init__(self):
        self.models: list[Poligonal_Model] = []
        self.scenes: list[Scene] = []
        self.flashes: list[Flash] = []
        self.cameras: list[Camera] = []
        if not len(self.models) or not len(self.scenes) or not len(self.flashes) or not len(self.cameras):
            # можно в одну строку все? или лучше разделить?
            raise f'Должен быть хотя бы 1 объект в свойствах'
        self._change_observers: list = [IModelChanger]

    def get_scene(self, id_: int):
        for scena in self.scenes:
            if id_ == scena.id_:
                return scena
            
    def notify_change(self, sender: IModelChanger):
        pass
