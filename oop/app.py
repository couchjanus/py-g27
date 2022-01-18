from geom.point import Point
from geom.line import Line


if __name__ == '__main__':
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    
    line = Line(p1, p2)
    
    print('Instance Line class = ', line)
    print('Line Length = ', line.length())