from abc import ABC, abstractmethod
    
    
class A(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod    
    def area(self):
        pass
    
    
class B(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def circle(self):
        pass
    
    
class C(A, B):
    def __init__(self, name):
        super().__init__(name)
        
    def circle(self):
        return 'circle'
    
    def area(self):
        return 'area'
        
        
start = C('name')
res = start.circle()
print(start.area(), res)