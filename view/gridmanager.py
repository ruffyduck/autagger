"""Module for management of all GUI elements"""


class GridManager:
    """Class that controls all GUI elements in a basic grid layout"""

    def __init__(self):
        self.columns = {}

    def add_element(self, element, ccolumn):
        """Adds new element to given line"""

        if ccolumn not in self.columns.keys():
            self.columns[ccolumn] = 1

        element.grid(row=self.columns[ccolumn], column=ccolumn)
        self.columns[ccolumn] += 1

    def reset(self):
        """Resets the complete grid. Should be called when redrawing GUI"""
        for column in self.columns:
            self.columns[column] = 1
