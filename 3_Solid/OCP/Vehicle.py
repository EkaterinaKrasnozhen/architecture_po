# мы не должны нагружать главный класс разными if, лучше реализовать конкретный метод в дочернем классе по своему

class Vehicle:
    def __init__(self, max_speed: int, type_: str):
        self._max_speed = max_speed
        self._type  = type_
        
    def get_max_speed(self) -> int:
        return self._max_speed
    
    def get_type(self) -> str:
        return self._type
    
    def calc_allowed_speed(self) -> int:
        return self._max_speed
    
    # def allowed_speed(self):
    #     if self._type == "car":
    #         return self._max_speed * 0.8