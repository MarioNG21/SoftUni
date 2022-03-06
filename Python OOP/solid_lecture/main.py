# single responsibility Principle


'''
you are given a list of shapes
Calculate the sum of their areas
And print it
'''
import math

from recepi import Rect, Circle


class ShapesController:
    @staticmethod
    def _cal_shape_area(shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi

    def print_areas_sum(self, shapes):
        area_sum = sum(self._cal_shape_area(s for s in shapes))
        return f"Area sum of shapes is: {area_sum}"


shapes = [Circle(10), Rect(4, 5)]
