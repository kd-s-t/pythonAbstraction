class Polygon():
    # abstract method
    def noofsides(self):
        pass

class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        return "I have 3 sides"

class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        return "I have 5 sides"

class Hexagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        return "I have 6 sides"

class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        return "I have 4 sides"
