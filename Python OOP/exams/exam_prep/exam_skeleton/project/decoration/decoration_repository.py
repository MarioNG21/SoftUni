'''
todo: the available decoration in the shop(all of the added decoration might come here)

'''
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

        return f"None"


