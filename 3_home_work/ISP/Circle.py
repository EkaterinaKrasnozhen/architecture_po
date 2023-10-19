# разделить функционал на несколько интерфейсов и выполнять только те интерфейсы, которые экземпляр может выполнить
from Shape import Shape

P = 3.14


class Square(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self):
        return self.radius * P

    def perimetr(self):
        return 2 * P * self.radius
