class A:
    def __init__(self,a):
        self.valA = a

    def display(self):
        print("A = ",self.valA)


ob = A(44)
ob1=A(43)
A.display(ob)
A.display(ob1)
