from zope.interface import implementer
from Model_Elements.Poligonal_Model import Poligonal_Model
from Model_Elements.Scene import Scene
from Model_Elements.Flash import Flash
from Model_Elements.Camera import Camera
from IModel_Changer import IModelChanger
from IModel_Changed_Observer import IModel_Changed_Observer
from Model_Elements.Texture import Texture
from Stuff.Angle import Angle3D
from Stuff.Point3D import Point3D
from Stuff.Color import Color


@implementer(IModelChanger)
class Model_Store():
    def __init__(self):
        self.models: list[Poligonal_Model] = []
        self.scenes: list[Scene] = []
        self.flashes: list[Flash] = []
        self.cameras: list[Camera] = []
        self.models.append(Poligonal_Model(textures=Texture()))
        self.scenes.append(Scene(models=list[Poligonal_Model], flashes=list[Flash], cameras=list[Camera]))
        self.flashes.append(Flash(angle=list[Angle3D], location=list[Point3D], color=list[Color], power=float))
        self.cameras.append(Camera())
        self._change_observers: list[IModel_Changed_Observer] = []

    def get_scene(self, id_: int):
        for scena in self.scenes:
            if id_ == scena.id_:
                return scena

    def notify_change(self, sender: IModelChanger):
        pass
