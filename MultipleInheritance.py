class Student:
    def setdata(self):
        self.name = input("Enter the name = ")
        self.roll = int(input("enter the rollnum = "))

    def display(self):
        print("ROLL  = ",self.roll)
        print("NAME  = ",self.name)

class Marks:
    def setMarks(self):
        self.m1 = int(input("Ente the marks1 = "))
        self.m2 = int(input("Ente the marks2 = "))
    def display(self):
        print("MARKS1  = ",self.m1)
        print("MARKS2  = ",self.m2)

class Report(Student,Marks):
    def cal(self):
        self.total = self.m1+self.m2
    def display(self):
        super().display()
        Marks.display(self)
        print("TOTAL  = ",self.total)

ob = Report()
ob.setdata()
ob.setMarks()
ob.cal()
ob.display()
