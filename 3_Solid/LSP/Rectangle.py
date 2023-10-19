from Quadrangle import Quadrangle


class Rectangle(Quadrangle):
    def __init__(self, length_1: float, length_2: float, length_3: float):
        self.length_1 = length_1
        self.length_2 = length_2
        self.length_3 = length_3
        
    def area(self):
        return super().area()