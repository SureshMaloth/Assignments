#map()
#Ex:1
def square(num):
    return num*num
numbers=eval(input("enter the nbr:"))
res=map(square,numbers)
print(list(res))

#Ex:2

print(list(map(int,input("enter the val:").split())))

#Ex:3
num1=[1,2,3,4]
num2=[5,6,7,8]
num3=[9,10,11,12]
res=map(lambda x,y,z:x+y+z,num1,num2,num3)
print(list(res))

#reduce()
from functools import reduce

def is_reduce(m,n):
    return m+n
number=eval(input("enter the list:"))
res=reduce(is_reduce,number)
print((res))

def is_square(m,n):
    return m*n
value=eval(input("enter the nbr:"))
result=reduce(is_square,value)
print(result)

list_values=eval(input("enter the list_val:"))
is_greater=reduce(lambda x,y:y if y>x else x,list_values)
print(is_greater)

#nested Functions
def is_square():
    def is_pos():
        print("Is Positive Value")
    print("Is Square Value")
    is_pos()
is_square()

def greet(word):
    def wish():
        return "Hello"
    return wish()+" Ram "+word
print(greet("How Are You"))

def is_str(a):
    print("hii")
    def value(b):
        c="This is Function"
        return a+" "+b+" "+c
    return value("Abhi")

res=is_str(input("enter the str:"))  
print(res)      


