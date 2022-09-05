class A:
    def __init__(self,a):
        self.a = a
        print("A init = ",self.a)

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
        print("B init = ",self.b)

class C(B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
        print("C init = ",self.c)

c = C(11,22,33)
