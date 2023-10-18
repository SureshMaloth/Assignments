#single Inheritanace
class College:
    def __init__(self,Cname,location):
        self.Cname=Cname
        self.location=location
    def display (self):
        print("My Clg Name is: ",self.Cname)
        print("My Clg location Is: ",self.location)
class Student(College):
    def __init__(self,Cname,location,Sname,id):
        College.__init__(self,Cname,location)
        self.Sname="Suresh"
        self.id="147Q1a"
    def res (self):
        print("This Is: ",self.Sname)
        print("My Roll No: ",self.id)

obj1=Student("TKR Clg","Lb Nagar","Suresh","147Q1a0")

obj1.res()
obj1.display()

#Multiple Inheritance

class Parent1:
    def fun1(self):
        print("This Is parent1")
class Parent2:
    def fun2(self):
        print("This is parent2")
class Child(Parent1,Parent2):
    def fun3(self):
        print("This Is Child Of Parents")
refObj=Child()
refObj.fun3()
refObj.fun2()
refObj.fun1()

#Multi Level Inheritance

class GrandParent:
    
    def display1(self):
        print("This Is My GrandParent Land")
class Parent(GrandParent):
    
    def display2(self):
        print("This is My parents Vechile BMW CAR")
        print("This is my Parents Furniture : King Size Bed")
class Child(Parent):
    
    def display3(self):
        print("This is my Fvt Bike: Duke 200")
object1=Child()
object1.display3()
object1.display2()
object1.display1()

#Hierarchical Inheritance

class Parent:

    def dis1(self):
        print("My Father name Is Ram age is 55")
class Child1(Parent):
    def dis2(self):
        print("Child1 Name is Abhi Age is 23")

class Child2(Parent):
    def dis3(self):
        print("Child1 Name is Charan Age is 25")

RefObject=Child1()
RefObject.dis2()
RefObject.dis1()

RefObject1=Child2()
RefObject1.dis3()
RefObject1.dis1()
