from Stuff.Point3D import Point3D
from Stuff.Angle import Angle3D
from Stuff.Color import Color

class Flash:
    def __init__(self, location: list[Point3D], angle: list[Angle3D], color: list[Color], power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power
        
    def rotate(angle: Angle3D) -> None:
        pass
    
    def move(point: Point3D) -> None:
        pass