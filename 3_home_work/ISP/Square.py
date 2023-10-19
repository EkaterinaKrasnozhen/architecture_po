from Shape import Shape
from Shape3D import Shape3D


class Square(Shape, Shape3D):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.width
    
    def perimetr(self):
        return self.width * 4
    
    def volume(self):
        return (self.width * 2) * self.height