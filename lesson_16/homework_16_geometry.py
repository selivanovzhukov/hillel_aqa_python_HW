from abc import ABC, abstractmethod
import math


class GeometryShape(ABC):
    # shape_name = None
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(GeometryShape):

    shape_name = 'Square'

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

class Rectangle(GeometryShape):

    shape_name = 'Rectangle'

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Triangle(GeometryShape):

    shape_name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))


geometry_shapes = [
    Triangle(3, 4, 5),
    Square(5),
    Rectangle(2, 3)
]

for shape in geometry_shapes:
    print(f'Shape: {shape.shape_name}, Area: {shape.area()}, Perimeter: {shape.perimeter()}')