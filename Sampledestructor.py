class A:
    def __init__(self,a):
        self.a = a
        print("A is getting created",a)

    def __del__(self):
        print("A is killed ",self.a)

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
        print("B is getting created",b)

    def __del__(self):
        super().__del__()
        print("B is killed ",self.b)

ob = B(22,33)
