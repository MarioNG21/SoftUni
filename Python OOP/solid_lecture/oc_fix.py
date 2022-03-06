import math

from recepi import Rect, Circle, Triangle, Square


class ShapeAreaCalculate:
    def _cal_shape_area(self, shape):
        return shape.area()

    def calculate_area(self, shapes):
        return sum(self._cal_shape_area(s) for s in shapes)


class ShapesAreaCalculatorWithTriangle(ShapeAreaCalculate):
    def _cal_shape_area(self, shape):
        if isinstance(shape, Triangle):
            return shape.side * shape.height / 2


class StdinPrinter:
    def print(self, message):
        print(message)


class FilePrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def print(self, message):
        with open(self.file_name, 'a') as file:
            file.writelines([message])


class ShapesController:
    shapes_area_calculator = ShapeAreaCalculate()
    printer = StdinPrinter()

    def print_areas_sum(self, shapes):
        area_sum = sum(self.shapes_area_calculator._cal_shape_area([x for x in shapes]))
        self.printer.print(f"Area sum of shapes is: {area_sum}")


shapes = [
    Circle(10), # 314
    Rect(4, 5), # 20
    Triangle(2, 5),# 5
    Square(5) # 25
]

ShapesController().print_areas_sum(shapes)
