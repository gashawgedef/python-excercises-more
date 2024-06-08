


a=input("Enter Name")
b=input("Enter Age")

class Student:

    def __init__(self,name,age,**marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name - ",self.name)
        print("Age - ",self.age)
        print("Marks - ",self.marks)


student =Student(a,b,Maths=87,English=89,Java=98,Python=90)
student.display()
dd=student.__dict__
print(dd)