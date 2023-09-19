 #Recursion function
#Ex:1
def square(n):
    if n==0:
        return 0
    return square(n-1)+n
n=int(input("enter the nbr:"))
res=square(n)
print(res)

#Ex:2
def sum_list(list_nbr):
    if len(list_nbr)==1:
        return list_nbr[0]
    return list_nbr[0]+sum_list(list_nbr[1:])
val_nbr=eval(input("enter the "))
print(sum_list(val_nbr))
#above function Gives limit Exceed
#Ex:3
def sum_of_list(list_nbr):
    total=0
    for i in list_nbr:
        if type(i)==type([]):
            total=total+sum_of_list(i)
        else:
            total+=i
    return total
list_values=eval(input("enter the list_nbr:"))#ex:[1,2,[3,4],5,[56,7]]

res=sum_of_list(list_values)
print(res)

#Lambda Function:

#(lambda parameters:expression)(arguments)
#Ex:1
print((lambda s:s*s)(int(input("enter the s val:"))))
#Ex:2
(lambda a:print("even")if a%2==0 else print("odd"))(int(input("enter n val:")))
#Ex:3
print((lambda marks:"Excellent"if marks>90 else("Good" if marks>75 else("Average" if marks>60 else "Fail")))(int(input("enter the marks:"))))


#Filter Function
#Ex:1
def str_val(i):
    if i not in "aeiou":
        return True
    
str_words="abcdefghijklmnopqrstuvwxyz"
res=filter(str_val,str_words)
print(list(res))
#Ex:2
def is_positive_nbr(nbr):
    
    if nbr>0:
        return True
numbers=eval(input("enter val:"))
is_filter_val=filter(is_positive_nbr,numbers)
print(list(is_filter_val))

#Ex:3


word=eval(input("enter the list:"))
res=filter(lambda i:i%2==0,word)
print(list(res))