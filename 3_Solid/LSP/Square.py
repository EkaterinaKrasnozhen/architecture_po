from Quadrangle import Quadrangle


class Square(Quadrangle):
    def __init__(self, length: float):
        self.length = length
        
    def area(self):
        return super().area()