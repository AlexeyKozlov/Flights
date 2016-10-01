from math import sqrt

class Point:
    def __init__(self,z,o):
        self.x=z
        self.y=o


    def distance(self,p2):
        dx=p2.x-self.x
        dy=p2.y-self.y
        return sqrt(dx*dx + dy*dy)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y