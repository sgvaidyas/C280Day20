class A:
    def __init__(self,a,b):
        self.valA = a
        self.valB = b
    def display(self):
        print("A = ",self.valA)
        print("B = ",self.valB)

class B(A):
    def __init__(self,a,b,c):
        #super().__init__(a)
        A.__init__(self,a,b)
        self.valC = c
    def display(self):
        super().display()
        print("C = ",self.valC)

ob = B(11,88,65)
ob.display()
