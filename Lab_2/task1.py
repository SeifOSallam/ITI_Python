from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, color):
        self.name = name
        self._color = color
    
    def setColor(self, color):
        self._color = color
    def getColor(self):
        return self._color
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, name, color, radius):
        try:
            self.radius = float(radius)
            if self.radius <= 0:
                self.radius *= -1
                raise Exception()
            super().__init__(name, color)
        except:
            print('Invalid input')
    
    def calculate_area(self):
        return self.radius*self.radius*3.14


class Square(Shape):
    def __init__(self, name, color, side):
        try:
            self.side = float(side)
            if self.side <= 0:
                self.side *= -1
                raise Exception()
            super().__init__(name, color)
        except:
            print('Invalid input')
        super().__init__(name, color)
        
    
    def calculate_area(self):
        return self.side*self.side
    

circle = Circle('first_circle', 'red', input('Enter the circle\'s radius length\n'))
print("The circle's area : " + str(circle.calculate_area()) + "\n")



square = Square('first_square', 'blue', input('Enter the square\'s side length\n'))
print("The square's area : " + str(square.calculate_area()) + "\n")


shape = Shape('first_shape', "blue")