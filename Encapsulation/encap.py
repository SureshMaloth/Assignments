#Encapsulation
class Institute:
    def __init__(self,course,tech,):
        self.course=course
        self.tech=tech
    def get_the_course(self):
        print(self.course+" "+self.tech)
    def set_the_course(self,tech1):
        self.tech=tech1
        print(self.tech)
obj1=Institute("Programming Language","Python")
obj1.get_the_course()
obj1.set_the_course("Java")
###

class Institute:
    def __init__(self,course,tech,):
        self.course=course
        self.__tech=tech
    def get_the_course(self):
        print(self.course+" "+self.__tech)
    def set_the_course(self,tech1):
        self.__tech=tech1
        print(self.__tech)
obj1=Institute("Programming Language","Python")
obj1.get_the_course()
obj1.set_the_course("Java")
print(obj1._Institute__tech)