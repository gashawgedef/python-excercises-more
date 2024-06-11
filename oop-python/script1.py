

class Salary:
    def __init__(self,pay,reward) -> None:
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay*12)+self.reward
    
class Employee:
    def __init__(self,name,position,pay,reward) -> None:
        self.name = name
        self.position = position
