# класс отвечает за свою маленькую часть(актор), функционал например калькуляции з/п лучше вынести в отдельный класс


class Employe:
    def __init__(self, name: str, surname: str, age: int, phone: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        
    def __str__(self):
        return f'Name: {self.name} Surname: {self.surname} phone: {self.phone}'