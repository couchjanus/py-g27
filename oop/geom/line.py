from geom.point import Point
import math

class Line:
    
    def __init__(self, p1 :Point, p2:Point) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self)->str:
        return "(({}, {}), ({}, {}))".format(self.p1.get_x(), self.p1.get_y(), self.p2.get_x(), self.p2.get_y())
        
    def length(self)->float:
        x = self.p2.get_x() - self.p1.get_x()
        y = self.p2.get_y() - self.p1.get_y()

        return math.sqrt(abs(x**2)+abs(y**2))
    

if __name__ == '__main__':
    p1 = Point(1,2)
    p2 = Point(3,4)
    
    line = Line(p1, p2)
    print(line)
    print(line.length())
    
