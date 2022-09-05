class A:
    def msg(self):
        print("I am in class A")
class B(A):
    def msg(self):
        print("I am in class B")
class C(A):
    def msg(self):
        print("I am in class C")
class D(B,C):
    pass

ob = D()
ob.msg()
