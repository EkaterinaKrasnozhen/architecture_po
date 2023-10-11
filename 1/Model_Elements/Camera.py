from Stuff.Point3D import Point3D
from Stuff.Angle import Angle3D


class Camera:
    def __init__(self, location: list[Point3D], angle: list[Angle3D]):
        self.location = location
        self.angle = angle
        
    def rotate(angle: Angle3D) -> None:
        pass
    
    def move(point: Point3D) -> None:
        pass