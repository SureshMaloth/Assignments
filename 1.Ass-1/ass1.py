#1. Condition Statements
num=int(input("enter the value:"))

if num%2==0:
    result="is Even"
else:
    result="is Odd"
print(result)


week_of_the_day=input("enter the day:")
if week_of_the_day == "Monday":
    print("Its Shiva's Day")
elif week_of_the_day == "Tuesday":
    print("Its Hanumas Day")
elif week_of_the_day == "Wednsday":
    print("Its Vinayakas Day")
elif week_of_the_day == "Thursday":
    print("Its Saibabas Day")
elif week_of_the_day == "Friday":
    print("Its LaxmiDevis Day")
elif week_of_the_day == "Saturday":
    print("Its Venteswara Swamis Day")
elif week_of_the_day == "Sunday":
    print("Its Surya Bhagavanas Day")

#2.Relational and LogicalOperators
number=int(input("enter the num:"))
if number>10 and 20>number:
    print("Is Number B/w 10 And 20")
elif number>30 and 40>number:
    print("Is Number B/w 30 And 40")
elif number>50 and 60>number:
    print("Is Number B/w 50 And 60")
elif number>70 and 80>number:
    print("Is Number B/w 70 And 80")
elif number>90 and 100>number:
    print("Is Number B/w 90 And 100")
else:
    print("Its above 100")


number=int(input("enter the num:"))
if number>10 or  20>number:
    print(number)
elif number>30 or 40>number:
    print(number)
elif number>50 or 60>number:
    print(number)
elif number>70 or 80>number:
    print(number)
elif number>90 or 100>number:
    print(number)
else:
    print(number)

#3.Create Table With Loops

#to create the table with while condition
number=int(input("enter number: "))
counter=1
while counter<=10:
    multiplication=number*counter
    result=str(number)+" X "+str(counter)+" = "+str(multiplication)
    print(result)
    counter=counter+1

#to create the table with for loop condition
num=int(input("enter num:"))
for i in range(1,num+1):
    multiplication=num*i
    result=str(num)+" X "+str(i)+" = "+str(multiplication)
    print(result)