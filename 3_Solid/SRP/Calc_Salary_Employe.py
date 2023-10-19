class CalcSalary:
    def __init__(self, base_salary):
        self.base_salary = base_salary
        
    def calc_salary(self, grade: float) -> float:
        return self.base_salary * grade