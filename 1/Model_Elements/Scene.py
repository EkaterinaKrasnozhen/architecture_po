from Poligonal_Model import Poligonal_Model
from Flash import Flash
from Camera import Camera


class Scene:
    def __init__(self, id_, models: list[Poligonal_Model], flashes: list[Flash], cameras: list[Camera]):
        self.id_ = id_
        if len(models):
            self.models = models
        else:
            raise f'В {self.models} должна быть минимум один объект {Poligonal_Model}'
        self.flashes = flashes
        if len(cameras):
            self.cameras = cameras
        else:
            raise f'В {self.cameras} должна быть минимум один объект {Camera}'

    def method1(example1: int) -> int:
        return example1

    def method2(example1: int, example2: int) -> int:
        return example1+example2
