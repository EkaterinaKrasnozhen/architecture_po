from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed, type_= 'car')
        
    def get_max_speed(self) -> int:
        return super().get_max_speed() * 0.8
    
car = Car(200)
print(car.get_max_speed())