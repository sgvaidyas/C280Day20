class Shape:
    def __init__(self):
        self.leng = 0
        self.bred = 0
        self.rad = 0

    def setLen(self):
        self.leng = float(input("Enter the length  ="))

    def setBred(self):
        self.bred = float(input("Enter the breadth  ="))

    def setRad(self):
        self.rad = float(input("Enter the radius  ="))

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.area = 0
        self.peri = 0

    def calculate(self):
        self.area = self.leng**2
        self.peri = self.leng * 4

    def display(self):
        print("LENGTH          = ",self.leng)
        print("AREA            = ",self.area)
        print("PERIMETER       = ",self.peri)

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.area = 0
        self.circumference = 0

    def calculate(self):
        self.area = 3.142*self.rad*self.rad
        self.circumference = 2*3.142*self.rad

    def display(self):
        print("RADIUS          = ",self.rad)
        print("AREA            = ",self.area)
        print("CIRCUMFERENCE   = ",self.circumference)

c = Circle()
c.setRad()
c.calculate()
c.display()



ob = Square()
ob.setLen()
ob.calculate()
ob.display()
