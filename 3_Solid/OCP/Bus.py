from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, max_speed: int):
        super().__init__(max_speed, type_='bus')
        
    def get_max_speed(self) -> int:
        return super().get_max_speed() * 0.5
    
car = Bus(200)
print(car.get_max_speed())