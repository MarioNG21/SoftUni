import math

from recepi import Rect, Circle


class ShapeAreaCalculate:
    # Valioation of OPEN/CLOSE PRINCIP if we want to add area of a trinagle we must create new instance
    def _cal_shape_area(self, shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi
        # New shape
        elif isinstance(shape, Triangle):
            pass
    def calculate_area(self, shapes):
        return sum(self._cal_shape_area(s) for s in shapes)


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

    def print_areas_sum(self, shapes):
        area_sum = sum(self._cal_shape_area(s for s in shapes))
        print(f"Area sum of shapes is: {area_sum}")
