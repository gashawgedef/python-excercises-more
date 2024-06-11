from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Square(Shape):
    def __init__(self,side) -> None:
        self.__side=side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):
        return self.__side*4
    
# shape_obje=Shape()
shape_square =Square(10)
print(shape_square.area(),shape_square.perimeter())