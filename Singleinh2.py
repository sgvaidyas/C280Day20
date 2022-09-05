class A:
    def __init__(self,a=0,b=0):
        self.valA = a
        self.valB = b
    def display(self):
        print("A = ",self.valA)
        print("B = ",self.valB)

class B(A):
    def __init__(self,c,a=0,b=0):
        #super().__init__(a)
        A.__init__(self,a,b)
        self.valC = c
    def display(self):
        super().display()
        print("C = ",self.valC)

ob = B(a=11,b=88,c=65)
ob.display()
