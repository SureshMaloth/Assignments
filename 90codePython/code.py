#Write a  programme to reverse an integer in a python
#1
num=123456
con_int_str=str(num)
reverse_num=int(con_int_str[::-1])
print(reverse_num)
print(type(reverse_num))
#2


n = int(input("Please give a number: "))
print("Before reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse)

print(123456//10)

#2 Write a programme in a python check whether an integer is armstrong num or not
num=153
str_num=str(num) 
length=len(str_num)
number=0
for i in str_num:
    number+=int(i)**length
if num==number:
    print("Is A ArmStrong Nmbr: ",number)
else:
    print("Is Not a Armstrong Num: ",number)

#2
num=int(input("enter the num:"))
total=0
temp=num
lenth_of_num=len(str(num))
while temp>0:
    digit=num%10
    total+=digit**lenth_of_num
    temp//=10
if total==temp:
    print("Is ArmStrong: ",num)
else:
    print("is not a ArmStrong Nbr:",num)


#3 Write a program to check given num prime or not

num=int(input("enter the num:"))
factor=0
for i in range(2,num):
    if num%i==0:
        factor+=1
    
if factor==0:
    print("It Is a Prime Num: ",num)
else:
    print("It Is Not a prime Nbr: ",num)


#4 Write a programme to print the Fibbonacci Series using iterative method

nbr=int(input("enter the nbr: "))
first,second=0,1
result=0
for i in range(0,nbr):
    if i<=1:
        result=i
    else:
        result=first+second
        first=second
        second=result
    
    print(result)
    
#5Write a programme to print the Fibbonacci Series using recursive method

def fibonacci(nbr):
    if nbr==0:
        return 0
    elif nbr==1:
        return 1
    else:
        return fibonacci(nbr-1)+fibonacci(nbr-2)
    
n=int(input("enter the nbr:"))
for i in range(0,n):
    print(fibonacci(i))
        

#6 Write a Programme in a python check wether a number is polindrome r not using iterative method

num=int(input("enter the nbr: "))
convert_int_to_str=int(str(num)[::-1])
if num==convert_int_to_str:
    print("It Is A polindrome")
else:
    print("It is Not a Polindrome")

reverse=0
while num != 0:
    reverse=reverse*10+num%10
    num=num//10
    
print(reverse)


    
#7 Write a Programme in a python check wether a number is polindrome r not using recursive method

n = int(input("please give a number : "))
def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))
def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome") 

#8Write a Programme in a python to find the gretest amoung three integers

num =int(input("enter the number: "))
print(num)
str_int=str(num)
first_num=str_int[0]
gretest_num=int(first_num)
for i in str_int:
    i=int(i)
    if i>gretest_num:
        gretest_num=i
print(gretest_num)

    
num_1=10
num_2=20
num_3=13
if num_1>=num_2 and num_1>=num_3:
    gretest=num_1
elif num_2>=num_1 and num_2>=num_3:
    gretest=num_2
else:
    gretest=num_3
print(gretest)

#9 write a program in a python to check if a number is binary or not

num=int(input("enter the num:"))
while num>0:
    n=num%10
    if n!=0 and n!=1:
        print("num is not a Binary")
        break
    num=num//10
    if num==0:
        print("Num is a binary")
#10 write a program in python to find the sum of digits of a number using recursion?
def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
num=12345
res=sum(num)
print(res)


#11 write a program in a python to swap two numbers without using third variable
a=10
b=8
a=a-b
b=a+b
a=b-a
print(a)
print(b)

#12 write a program in a python to swap two numbers with using third variable
a=10
b=8
c=a
a=b
b=c
print(a)
print(b)

#13 write a program in python to find prime factors of given integer

def prime(num):
    factor=[]
    divisor=2
    while num>1:
        while num%divisor==0:
            factor.append(divisor)
            
            num=num//divisor
        divisor+=1
    return factor
n=int(input("enter the num:"))
res=prime(n)
print(res)

#14 write a python program to add  two integer without using arthimetic operator?

def add_numbers(x, y):
    while y != 0:
        temp = x & y
        x = x ^ y
        y = temp << 1
    return x
 
num1 = 10
num2 = 15
sum_result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")


#15 write a program in python to find given number is perfect r not

nbr=int(input("enter the perfect nbr:"))
total=0
for i in range(1,nbr):
    if nbr%i==0:
        total+=i
if total==nbr:
    print("It Is A Perfect Nbr : ",nbr)
else:
    print("It Is Not A Perfect Nbr: ",nbr)

#16 python program to find the avg of numbers with explanations
avg_num=123456789
str_int=str(avg_num)
length_of_avg_numbrs=len(str_int)
avg_num_length=int(length_of_avg_numbrs)//2
pyth_avg_num=str_int[avg_num_length]
print(pyth_avg_num)

#2
size_of_num=int(input("enter the size:"))
sum_size=0
for i in range(size_of_num):
    n=int(input("enter the avg nbrs:"))
    devisor=n/size_of_num
    sum_size+=devisor
print(sum_size)

#17. python program to calculate factorial using iterative method

nbr=int(input("enter the factorial nbr:"))
sum_factorial=1
for i in range(1,nbr+1):
    sum_factorial*=i
print(sum_factorial)

#18 python program to calculate factorial using recursion

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
nbr=int(input("Enter The Factorial Nbr:"))
res=factorial(nbr)
print(res)

#19 python program to check  a given nbr is even or odd

nbr=int(input("enter the even r odd nbr:"))

if nbr%2==0:
    print("This Nbr Is Even")
else:
    print("This Nbr Is Odd")

#20 python program to print first n prime numbers with explanations

num=int(input("enter the first n prime nbr:"))
factor=[]

for i in range(2,num+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        factor.append(i)
print(factor)

#21 python program to print prime numbers given range

m=int(input("enter range1:"))
n=int(input("enter range2:"))
factor=[]

for i in range(m,n+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        factor.append(i)
print(factor)

#22 python program to find smallest number amoung three

a=int(input("enter first smallest numbe:"))
b=int(input("enter second smallest numbe:"))
c=int(input("enter Third smallest numbe:")) 
if a<b and a<c:
    smallest_num=a
elif b<c and b<a:
    smallest_num=b
else:
    smallest_num=c
print(smallest_num)

        

    
#23 python program to calculate the power using the POW method

base=int(input("enter the base num:"))
exponent=int(input("enter the exponent:"))
print(pow(base,exponent))

#24 python program to calculate the power without using POW of function using for loop
for i in range(1):
    base=int(input("enter the base num:"))
    exponent=int(input("enter the exponent:"))
    print(base**exponent)

#25 python program to calculate the power without using POW function using while loop

base=int(input("enter the base num:"))
exponent=int(input("enter the exponent:"))
counter=0
while counter<1:
    print(base**exponent) 
    counter+=1
#26 python program to calculate the square of a given number

num=int(input("enter the square num:"))
print(num**2)

#27 python program to calculate the cube of a given number
num=int(input("enter the cube num:"))
print(num**3)
#28 python program to calculate the square root of a given number
num=int(input("enter the square num:"))
print(num**0.5)
#29 python program to calculate the LCM of given two numbers

num1=int(input("enter the lcm num1:"))
num2=int(input("enter the lcm num2:"))
if num1>num2:
    gretest_nbr=num1
else:
    gretest_nbr=num2
for i in range(gretest_nbr,num1*num2):
    if i%num1==0 and i%num2==0:
        gretest_nbr=i
print(gretest_nbr)
#30 python program to find GCD or HCF of two numbers

num1=int(input("enter the hcf num1:"))
num2=int(input("enter the hcf num2:"))
if num1>num2:
    lower_nbr=num2
else:
    lower_nbr=num1
for i in range(1,lower_nbr+1):
    if num1%i==0 and num2%i==0:
        lower_nbr=i
print(lower_nbr)