# главный класс не должен зависеть напрямую от каких-то подклассов
from Engine import Engine
from Diesel import Diesel
from Petrol import Petrol


class Car:
    def __init__(self, model: str, engine: Engine):
        self.model = model
        self.engine = engine
        

if __name__ == '__main__':
    petrol = Petrol()      
    diesel = Diesel() 
    car1 = Car('toyota', petrol)
    car2 = Car('bmv', diesel)
    car1.engine.start()
    car2.engine.start()