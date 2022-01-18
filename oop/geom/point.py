class Point:
    '''
    Point on the plane
    '''
    def __init__(self, x :float = 0.0, y :float = 0.0) -> None:
        # self.__x = x
        # self.__y = y
        
        self.set_x(float(x))
        self.set_y(float(y))
        
    def get_x(self)->float:
        return self.__x
    
    def set_x(self, x:float)->None:
        self.__x = x
    
    def get_y(self)->float:
        return self.__y
    
    def set_y(self, y:float)->None:
        self.__y = y
        
    def __str__(self)->str:
        return "({}, {})".format(self.__x, self.__y)

if __name__ == '__main__':
    p1 = Point(1,2)
    p2 = Point(3,4)
    # print(dir(Point))
    # print(p.__doc__)
    print(p1.__str__())
    print(p1)
    
    # p2.set_x(1.1)
    print(p1.get_x()) 
    print(p2.get_x())